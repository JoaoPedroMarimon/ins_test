import logging
import os
import time
import serial
import src
import cv2

from datetime import datetime
from logging import exception

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

    ihm = src.IHM() # Abre a IHM

    index_modelo = None  # Inicializa o index_modelo vazio

    # Faz a leitura dos modelos no json
    for index, produto in enumerate(config['products']):
        print(f"Posição: {index}, Nome do produto: {produto['name']}")

    # Esse while enquanto a tela esta aberta
    while ihm.is_alive():

        # Modificar aqui para a função de modelo vindo da IHM
        while index_modelo is None:
            ser.write(b'y')  # Coloca o arduino em standby (inicialmente ja ta): entra na etapa -1 inexistente

            try:
                index_modelo = int(input("Digite a posição do produto: "))
                if 0 <= index_modelo < 3:
                    ser.write(b'x') # Tira o arduino do standby: entra na etapa 0
                    break
                else:
                    print(f"Índice inválido. Digite um número entre 0 e {len(config['products']) - 1}.")
            except ValueError:
                print("Por favor, digite um número válido.")

        if index_modelo is not None:

            produto_config = config['products'][index_modelo]
            status = produto_config['status']

            pad_inspec.config = config["products"][index_modelo]["pad-inspection"]
            pad_inspec.templates_path = f"./samples/{config['products'][index_modelo]['name']}/templates"

            read = ser.read().strip(b"\r\n")

            if read == b"p":
                frame = capturar_frame(camera)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                '''
                Status possíveis:
                    A: apenas salva o frame (pasta geral > sem_classif)
                    B: inspeciona e salva o frame (pasta geral > com_classif > OK ou NOK)
                    C: inspeciona e classifica o frame
                    D: inspeciona, classifica e salva o frame (pasta teste > OK ou NOK)
                '''

                if status in ('A'):
                    salvar_imagem_processada(frame=frame,
                                             pasta=f"./samples/{config['products'][index_modelo]['name']}/geral/sem_clasif",
                                             nome_imagem=f"imagem_{produto_config['name']}_{timestamp}.jpg")

                if status in ('B'):
                    frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                    if inspecao_ok:
                        # aqui deve enviar o resultado APROVADO
                        salvar_imagem_processada(frame=frame,
                                                 pasta=f"./samples/{config['products'][index_modelo]['name']}/geral/com_clasif/ok",
                                                 nome_imagem=f"imagem_{produto_config['name']}_{timestamp}.jpg")
                    else:
                        # aqui deve enviar o resultado REPROVADO
                        salvar_imagem_processada(frame=frame,
                                                 pasta=f"./samples/{config['products'][index_modelo]['name']}/geral/com_clasif/nok",
                                                 nome_imagem=f"imagem_{produto_config['name']}_{timestamp}.jpg")

                if status in ('C'):
                    frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                    classificar_resultado(inspecao_ok)
                    if inspecao_ok:
                        # aqui deve enviar o resultado APROVADO
                    else:
                        # aqui deve enviar o resultado REPROVADO


                if status in ('D'):
                    frame_processado, inspecao_ok = inspecionar_frame(frame, pad_inspec)
                    classificar_resultado(inspecao_ok)
                    if inspecao_ok:
                        # aqui deve enviar o resultado APROVADO
                        ser.write(b'o')
                        salvar_imagem_processada(frame=frame,
                                                 pasta=f"./samples/{config['products'][index_modelo]['name']}/teste/ok",
                                                 nome_imagem=f"imagem_{produto_config['name']}_{timestamp}.jpg")
                    else:
                        # aqui deve enviar o resultado REPROVADO
                        ser.write(b'n')
                        salvar_imagem_processada(frame=frame,
                                                 pasta=f"./samples/{config['products'][index_modelo]['name']}/teste/nok",
                                                 nome_imagem=f"imagem_{produto_config['name']}_{timestamp}.jpg")

            # aqui recebe o aviso de limite reprovadas do arduino
            # deve chamar a funcao p/ abrir popup
            if read == b"w":
                print("enviado aviso de limite excedido p/ tela")

if __name__ == '__main__':
    main()