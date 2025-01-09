#!/bin/bash

sudo apt-get install openssh-server -y
sudo apt-get install zenity -y
sudo systemctl start ssh


DIR="$(dirname "$(realpath "$0")")"
# Check if the virtual environment directory exists, if not, create it
if [ ! -d "$DIR/venv" ]; then
    python3 -m venv "$DIR/venv"
fi
source "$DIR/venv/bin/activate"
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r "$DIR/requirements.txt" || { echo "Failed to install requirements"; exit 1; }
deactivate


cat > "$DIR/run.sh" << EOL
#!/bin/bash
source "$DIR/venv/bin/activate"
cd $DIR
"$DIR/venv/bin/python3" "$DIR/main.py" "\$@"
EOL

chmod +x "$DIR/run.sh"
chmod +x "$DIR/main.py"

# Define the application to start in each reboot
sudo touch /etc/systemd/system/inspecao-tampografia-switch-8p.service
sudo chmod 777 /etc/systemd/system/inspecao-tampografia-switch-8p.service
sudo cat > /etc/systemd/system/inspecao-tampografia-switch-8p.service << EOL
[Unit]
Description=Inspeção Tampografia Switch 8p
After=graphical.target

[Service]
Type=simple
ExecStart="$DIR/run.sh"
User=tampografia
Environment="QT_QPA_PLATFORM=wayland"  
Environment="WAYLAND_DISPLAY=wayland-0"  
Environment="XDG_RUNTIME_DIR=/run/user/1000"  
[Install]
WantedBy=graphical.target


EOL
sudo systemctl enable inspecao-tampografia-switch-8p.service 
sudo systemctl start inspecao-tampografia-switch-8p.service 


# Define the destination path for the desktop entry
dest_path="$HOME/Área de Trabalho/"

# Create the .desktop entry file for the application
cat > "$dest_path/inspec_tamp_switch.desktop" << EOL
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Inspeção Tampografia Switch 8p
Terminal=true
Exec=$DIR/run.sh
Icon=$DIR/src/static/inspec_tamp_switch.png
X-GNOME-Autostart-enabled=true
EOL

# Update the desktop database to register the new application
update-desktop-database "$dest_path"


CONFIRMATION=$(zenity --question --title="Aviso" \
--text="É necessário reiniciar a máquina para aplicar as configurações, reiniciar agora?" \
--no-wrap)

if [ $? -eq 0 ]; then
  reboot
fi

