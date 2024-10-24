import logging
import os
import time

import cv2
import serial
import src
import cv2

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

def salvar_imagem_processada(frame, pasta=".", nome_imagem="imagem_processada.jpg"):
    """
    Salva a imagem processada em um diretório especificado.

    :param frame: A imagem processada (frame da câmera).
    :param pasta: Caminho da pasta onde a imagem será salva (padrão é o diretório atual).
    :param nome_imagem: Nome do arquivo da imagem (padrão é 'imagem_processada.png').
    """
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
    return frame_processado, inspecao_ok

def classificar_resultado(inspecao_ok):
    """
    Classifica o resultado da inspeção e imprime o status.

    :param inspecao_ok: Resultado da inspeção (True se passou, False se reprovou).
    :return: Retorna 'OK' ou 'NOK' de acordo com o resultado da inspeção.
    """
    if inspecao_ok:
        print("OK")
        #return "OK"
    else:
        print("NOK")
        #return "NOK"

def processar_frame(frame, pad_inspec, status, pasta=".", nome_imagem="imagem_processada.jpg"):
    """
    Processa o frame da câmera de acordo com o status do produto.

    :param frame: O frame capturado da câmera.
    :param pad_inspec: Objeto da classe PadInspection para processar e inspecionar o frame.
    :param status: String que define a ação ('SAVE', 'INSPSAVE', 'INSPSAVECLASSIFY', 'INSPCLASSIFY').
    :param pasta: Diretório onde a imagem será salva (se necessário).
    :param nome_imagem: Nome do arquivo da imagem a ser salva (se necessário).
    :return: Retorna o resultado da classificação (OK/NOK) se houver inspeção e classificação.
    """
    inspecao_ok = None
    resultado_classificacao = None

    if status == "SAVE":
        # Apenas salvar a imagem capturada
        salvar_imagem_processada(frame, pasta=pasta, nome_imagem=nome_imagem)

    elif status == "INSPSAVE":
        # Inspecionar e salvar a imagem
        frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
        salvar_imagem_processada(frame_processado, pasta=pasta, nome_imagem=nome_imagem)
        print(f"Inspecao:{inspecao_ok}")

    elif status == "INSPSAVECLASSIFY":
        # Inspecionar, salvar e classificar
        frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
        salvar_imagem_processada(frame_processado, pasta=pasta, nome_imagem=nome_imagem)
        resultado_classificacao = classificar_resultado(inspecao_ok)

    elif status == "INSPCLASSIFY":
        # Inspecionar e classificar (sem salvar)
        frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
        resultado_classificacao = classificar_resultado(inspecao_ok)

    return resultado_classificacao

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

    ihm = IHM(config["products"])
    while ihm.is_alive():
        if ihm.get_model_index() is not None and ser.read() == "I":
            index = ihm.get_model_index()
            pad_inspec = src.PadInspection(templates_path=f"./templates/{config['products'][index]['name']}")
            pad_inspec.config = config["products"][index]["pad-inspection"]

            frame = capturar_frame(camera)
            if frame is None:
                break

            produto_config = config['products'][index]
            status = produto_config['status']

            resultado_classificacao = processar_frame(
                frame,
                pad_inspec,
                status=status,
                pasta="./imagens_processadas",
                nome_imagem=f"imagem_{produto_config['name']}.jpg"
            )

            # Exibe o resultado da classificação se houver
            if resultado_classificacao is not None:
                print(f"Resultado da classificação: {resultado_classificacao}")

            time.sleep(5)

if __name__ == '__main__':
    config: dict = src.load_json_configfile(src.CONFIGFILE_PATHNAME, src.DEFAULT_CONFIGFILE)
    ihm = IHM(config["products"])
    ihm.run_ihm()
    while ihm.is_alive():
        if ihm.get_model_index():
            print(f"{ihm.get_model_index()}")
    main()

