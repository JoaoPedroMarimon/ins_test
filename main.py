import logging
import os
import time
from datetime import datetime

import src

def main():
    args = src.main_parse()
    src.init_logging(logging.WARNING, stream_handler=True, log_directory=".", debug=args.debug)
    logging.warning(f"init with {args}")

    if args.subparser is not None or args.serial_data:
        src.execute_parse(args)
        return

    '''port: str = src.get_port_connection()
    if not port and not args.no_serial and not args.serial_port:
        msg = f"Não foi possível encontrar a porta do Arduino, portas listadas: {src.get_all_ports()}"
        raise ConnectionError(msg)
    port = args.serial_port if args.serial_port else port
    #ser = src.SerialController(port, args.no_serial, args.debug)'''

    config: dict = src.load_json_configfile("./config.json")

    url = src.get_rtsp_url(**src.DEFAULT_CONFIGFILE["camera"])
    logging.debug(url)
    succeeded, timed_out = src.try_camera_connection(url, timeout=5.8)
    if not succeeded or timed_out:
        msg = "Não foi possível se conectar com a câmera, é possível que esteja desconectada."
        raise ConnectionError(msg)
    camera = src.ThreadedVideoCapture(url, exception=True, timeout=20)

    #instantiates the interface for product selection and test status, it uses camera subtype (must be configured)
    #intf = src.Interface(src.get_rtsp_url(subtype=1, **config["camera"]), configfile_dir="./src")

    pad_inspec = src.PadInspection(True, templates_path="./templates")
    pad_inspec.config = config["pad-inspection"]

    while True:
        ret, frame = camera.read()
        frame, cfg = pad_inspec.frame_inspect(frame)
        inspecao_ok = pad_inspec.validate_config_result(cfg)
        if inspecao_ok:
            print("Tudo ok")
        else:
           print ("teste reprovado")

if __name__ == '__main__':
    main()