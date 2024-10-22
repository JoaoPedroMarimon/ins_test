import time

import src
from src.IHM.interface import Interface
if __name__ == '__main__':
    config: dict = src.load_json_configfile(src.CONFIGFILE_PATHNAME, src.DEFAULT_CONFIGFILE)
    inter = Interface(config['products'])
    print(config['products'])
    inter.run_interface()
    while inter.is_alive():
        time.sleep(1)
        print("teste")


