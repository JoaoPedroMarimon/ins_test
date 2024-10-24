import logging
import os
import time

import cv2
import serial
import src

from datetime import datetime
from logging import exception
from src import IHM
from src import Interface
from src.IHM.src.components.communication.ihm_client import IHMClient
from src.IHM.src.components.video_preview.videoqthread import get_rtsp_url


def verificar_conexao_serial(args):
    """
    Função que tenta se conectar à porta serial até ter sucesso.
    """
    ser = None  # Inicializando a variável
    while ser is None:
        try:
            port = src.get_port_connection()  # Tenta obter a porta de conexão
            if not port and not args.no_serial and not args.serial_port:
                print(f"Não foi possível encontrar a porta do Arduino. Tentando novamente...")
                print(f"Portas disponíveis: {src.get_all_ports()}")
                time.sleep(3)  # Espera 3 segundos antes de tentar novamente
            else:
                port = args.serial_port if args.serial_port else port
                ser = src.SerialController(port, args.no_serial, args.debug)  # Tentativa de criar o controlador serial
                print(f"Conectado com sucesso na porta {port}.")
        except Exception as e:
            print(f"Erro ao conectar na porta serial {port}: {e}")
            ser = None  # Garante que ele tente novamente no loop
            time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    return ser

def verificar_conexao_camera(config_camera):
    """
    Função que tenta se conectar à câmera até ter sucesso.
    """
    camera = None
    url = src.get_rtsp_url(**config_camera)  # Obtém a URL RTSP
    logging.debug(url)  # Adiciona URL da câmera no log para depuração

    while camera is None:
        try:
            print(f"Tentando conectar à câmera com URL {url}...")
            succeeded, timed_out = src.try_camera_connection(url, timeout=5.8)
            if not succeeded or timed_out:
                print("Não foi possível se conectar com a câmera, tentando novamente...")
                time.sleep(3)  # Espera 3 segundos antes de tentar novamente
            else:
                camera = src.ThreadedVideoCapture(url, exception=True, timeout=20)  # Conexão bem-sucedida
                print("Conectado à câmera com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar à câmera: {e}")
            camera = None  # Garante que ele tente novamente no loop
            time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    return camera

def tentar_enviar_reproved(ser, args):
    """
    Função que verifica a conexão serial antes de enviar ser.reproved().
    Caso a conexão seja perdida, a função tentará reconectar e só então enviar o comando.
    """
    while True:
        # Verifica se a conexão serial está ativa
        if ser is None:
            print("Conexão serial perdida. Tentando reconectar...")
            ser = tentar_conectar_serial(args)  # Tenta reconectar
        try:
            ser.reproved()  # Envia o comando após reconectar
            print("Comando 'reproved' enviado com sucesso.")
            break  # Sai do loop se o comando for enviado com sucesso
        except Exception as e:
            print(f"Erro ao enviar reproved: {e}. Verificando conexão serial...")
            ser = None  # Marca a conexão como perdida e tenta reconectar

def main():
    args = src.main_parse()
    src.init_logging(logging.WARNING, stream_handler=True, log_directory=".", debug=args.debug)
    logging.warning(f"init with {args}")

    if args.subparser is not None or args.serial_data:
        src.execute_parse(args)
        return

    # Conectar à porta serial
    ser = verificar_conexao_serial(args)

    # Conectar à câmera
    camera = verificar_conexao_camera(src.DEFAULT_CONFIGFILE["camera"])

    # Carrega a configuração do arquivo JSON
    config: dict = src.load_json_configfile(src.CONFIGFILE_PATHNAME, src.DEFAULT_CONFIGFILE)

    pad_inspec = src.PadInspection(templates_path=f"./templates/{config['products'][0]['name']}")
    pad_inspec.config = config["products"][0]["pad-inspection"]

    print("Tela 1")

    while True:
        comando = input("Digite 'tela 2': ")
        if comando == "tela 2":
            print(f"Tela 2 selecionada")

            # Iniciar loop de inspeção
            while True:
                ret, frame = camera.read()  # Captura o frame da câmera
                if not ret:
                    print("Erro ao capturar frame da câmera")
                    break  # Se a captura falhar, sai do loop

                # Realiza a inspeção no frame capturado
                frame, cfg = pad_inspec.frame_inspect(frame)
                inspecao_ok = pad_inspec.validate_config_result(cfg)

                # Verifica o resultado da inspeção
                if inspecao_ok:
                    print("Tudo ok")
                else:
                    print("Teste reprovado")
        else:
            print("Opção inválida")

if __name__ == '__main__':
    config: dict = src.load_json_configfile(src.CONFIGFILE_PATHNAME, src.DEFAULT_CONFIGFILE)
    ihm = IHM(config["products"])
    ihm.run_ihm()
    main()

