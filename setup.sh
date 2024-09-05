#!/bin/bash

DIR="$(dirname "$(realpath "$0")")"

# Check if the virtual environment directory exists, if not, create it
if [ ! -d "$DIR/venv" ]; then
    python3 -m venv "$DIR/venv"
fi
source "$DIR/venv/bin/activate"
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r "$DIR/requirements.txt" || { echo "Failed to install requirements"; exit 1; }
deactivate

sudo apt-get install openssh-server -y
sudo apt-get install zenity -y
sudo systemctl start ssh

cat > "$DIR/run.sh" << EOL
#!/bin/bash
source "$DIR/venv/bin/activate"
cd $DIR
"$DIR/venv/bin/python3" "$DIR/main.py" "\$@"
EOL

chmod +x "$DIR/run.sh"
chmod +x "$DIR/main.py"

# Define the destination path for the desktop entry
dest_path="$HOME/.local/share/applications"

# Create the .desktop entry file for the application
cat > "$dest_path/inspec_tamp_switch.desktop" << EOL
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Inspeção Tampografia Switch 8p
Terminal=true
Exec=$DIR/run.sh
Icon=$DIR/src/static/inspec_tamp_switch.png
EOL

# Update the desktop database to register the new application
update-desktop-database "$dest_path"

CONFIRMATION=$(zenity --question --title="Aviso" \
--text="É necessário reiniciar a máquina para aplicar as configurações, reiniciar agora?" \
--no-wrap)

if [ $? -eq 0 ]; then
  reboot
fi

