import logging
import os
import time
from time import sleep, pthread_getcpuclockid
from tkinter.messagebox import RETRY

import serial
import src
import cv2

from datetime import datetime
from logging import exception

from src.ArduinoPlaceHolder.arduino import Arduino


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

def capturar_frame(camera):
    """
    Captura um frame da câmera.

    :param camera: Objeto da câmera.
    :return: O frame capturado.
    """
    ret, frame = camera.read()
    if not ret:
        print("Erro ao capturar frame")
        return None
    return frame

def salvar_imagem(frame, nome_produto, posicao, pasta, timestamp):

    pasta=f"./samples/{nome_produto}/{posicao}/{pasta}"
    nome_imagem=f"imagem_{nome_produto}_{timestamp}.jpg"

    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho_imagem = os.path.join(pasta, nome_imagem)
    cv2.imwrite(caminho_imagem, frame)
    print(f"Imagem processada e salva em: {caminho_imagem}")

def inspecionar_frame(frame, pad_inspec):
    """
    Aplica a inspeção à imagem capturada.

    :param frame: O frame capturado da câmera.
    :param pad_inspec: Objeto da classe PadInspection que realiza a inspeção.
    :return: Retorna o frame processado e o resultado da inspeção (True se passou, False se reprovou).
    """
    frame_processado, cfg = pad_inspec.frame_inspect(frame)
    inspecao_ok = pad_inspec.validate_config_result(cfg)
    markers_position = [{"name": class_["name"], "region": class_["region"]} for class_ in cfg["classes"] if class_["found"] == False]
    return frame_processado, markers_position, inspecao_ok

def classificar_resultado(inspecao_ok):
    """
    Classifica o resultado da inspeção e imprime o status.

    :param inspecao_ok: Resultado da inspeção (True se passou, False se reprovou).
    :return: Retorna 'OK' ou 'NOK' de acordo com o resultado da inspeção.
    """
    if inspecao_ok:
        print("OK")
    else:
        print("NOK")

def main():

    args = src.main_parse()
    src.init_logging(logging.WARNING, stream_handler=True, log_directory=".", debug=args.debug)
    logging.warning(f"init with {args}")

    if args.subparser is not None or args.serial_data:
        src.execute_parse(args)
        return

    ser = verificar_conexao_serial(args)
    camera = verificar_conexao_camera(src.DEFAULT_CONFIGFILE["camera"])
    config = src.load_json_configfile(src.CONFIGFILE_PATHNAME, src.DEFAULT_CONFIGFILE)

    pad_inspec = src.TemplateInspection()

    # Faz a leitura dos modelos no json
    for index, produto in enumerate(config['products']):
        print(f"Posição: {index}, Nome do produto: {produto['name']}")

    ihm = src.IHM(config['products'])
    ihm.run_ihm()

    while ihm.is_alive():
        index_modelo = ihm.get_model_index()

        if index_modelo is None:
            ser.write(b'y')
            sleep(1)
            print("Enviando 'y' para standby")

        elif index_modelo is not None:
            ser.write(b'x')
            print(f"Modelo selecionado: {index_modelo}")  # Imprime apenas uma vez na mudança para valor válido

            produto_config = config['products'][index_modelo]
            pad_inspec.config = produto_config["pad-inspection"]
            pad_inspec.templates_path = f"./samples/{produto_config['name']}/templates"
            status = produto_config['status']

            # Laço contínuo para monitorar a comunicação serial
            while index_modelo is not None:
                if ser.in_waiting > 0:
                    read = ser.readline().strip(b"\r\n")
                    print(f"Recebido: {read}")

                    if read == b"p1" or read == b"p2":
                        frame = capturar_frame(camera)
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        posicao = "posicao_1" if read == b"p1" else "posicao_2"
                        if status == 'A':
                            salvar_imagem(frame, produto_config['name'], posicao, "geral/sem_clasif", timestamp)
                        elif status == 'B':
                            frame_processado,_, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                            pasta = "geral/com_clasif/ok" if inspecao_ok else "geral/com_clasif/nok"
                            salvar_imagem(frame, produto_config['name'], posicao, pasta, timestamp)
                        elif status == 'C':
                            frame_processado,_, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                            classificar_resultado(inspecao_ok)
                            ihm.send_approved() if inspecao_ok else ihm.send_reproved()
                            ser.write(b'o' if inspecao_ok else b'n')
                        elif status == 'D':
                            frame_processado, markers, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                            classificar_resultado(inspecao_ok)
                            pasta = "teste/ok" if inspecao_ok else "teste/nok"
                            print("inspeção: ",inspecao_ok)
                            salvar_imagem(frame, produto_config['name'], posicao, pasta, timestamp)
                            ihm.send_markers(markers)
                            ihm.send_approved() if inspecao_ok else ihm.send_reproved()
                            ser.write(b'o' if inspecao_ok else b'n')

                    elif read == b"w":
                        ihm.open_limit_exceed_screen()
                        print("enviado aviso de limite excedido p/ tela")

                    elif read == b"k":
                        ihm.new_cycle() # clean history
                index_modelo = ihm.get_model_index()

                if index_modelo is None:
                    print("Modelo desmarcado, retornando ao modo de espera.")
                    break  # Sai do loop e retorna ao início do loop principal

                time.sleep(0.1)  # Pequena pausa para evitar leitura excessiva

if __name__ == "__main__":
    main()