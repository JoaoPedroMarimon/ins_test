import json
import logging
import os
import queue
import time
import threading
import warnings
import multiprocessing
from tkinter.messagebox import showerror
from typing import Callable

import cv2
import numpy as np
from serial.tools.list_ports import comports

from .logger import handle_exception


def load_json_configfile(file_path: str, default: dict | list = None) -> dict | list:
    if not os.path.exists(file_path):
        if default is not None:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        else:
            msg = f"O caminho do arquivo não existe, verifique '{file_path}'."
            raise NotADirectoryError(msg)

    if not os.path.isfile(file_path):
        if default is not None:
            with open(file_path, 'w') as f:
                json.dump(default, f, indent=2)
            return default

        else:
            msg = f"O arquivo não existe, verifique '{file_path}'."
            raise FileNotFoundError(msg)

    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def dump_json_configfile(file_path: str, config: dict | list) -> None:
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=2)


def get_port_connection() -> str:
    """
    Returns the port name of the first connected USB serial device found in `serial.tools.list_ports.comports()`.

    It looks for common device patterns like '/ttyACM' and '/ttyUSB' in the port names.
    """
    for cm in comports():
        if "/ttyACM" in cm.device:
            return cm.device

        elif "/ttyUSB" in cm.device:
            return cm.device

    return ""


def get_all_ports() -> list[str]:
    """
    Returns all the port names connected, ignoring the `ttyS0` port.
    """
    return [cm.device for cm in comports() if cm.device != "/dev/ttyS0"]


class ThreadedVideoCapture(cv2.VideoCapture):
    @handle_exception(1)
    def __init__(self, url: str, delay=0.002, timeout=5, exception=True, do_init=True):
        self.url = url
        self._delay = delay
        self._timeout = timeout
        self._queue = queue.SimpleQueue()
        self._thread = threading.Thread(target=self._reader)
        self._thread.daemon = True
        self._keep_running = True
        self._read_request = False

        if do_init:
            cv2.VideoCapture.__init__(self, url)
            if not self.isOpened():
                msg = "Não foi possível se conectar com a câmera, é possível que esteja desconectada."
                if exception:
                    raise ConnectionError(msg)
                else:
                    logging.error(msg)
            self._thread.start()

        else:
            def dummy_function():
                return False, None

            self.read = dummy_function
            self.close = dummy_function

    def _reader(self) -> None:
        while self._keep_running:
            if not self.isOpened():
                self.reconnect()
                continue
            time.sleep(self._delay)
            ret = self.grab()
            if not ret:
                self.reconnect()
                continue

            if not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    pass
            if self._read_request:
                self._queue.put(self.retrieve()[1])

    def read(self) -> tuple[bool, np.ndarray | None]:
        self._read_request = True
        try:
            frame = self._queue.get(timeout=self._timeout)
        except Exception as e:
            logging.exception('Não foi possível obter uma imagem da câmera, é possível que tenha sido desconectada.')
            ret, frame = False, None
        else:
            ret = True
        self._read_request = False
        return ret, frame

    def reconnect(self) -> None:
        logging.critical('Algum erro ocorreu com a câmera, não houve retorno de imagem, tentando reconectar...')
        attempts = 1
        start = time.time()
        self.release()
        self.open(self.url)
        while not self.isOpened():
            self.release()
            self.open(self.url)
            attempts += 1
            time.sleep(1)
        logging.warning(f'A câmera se reconectou novamente após {attempts} tentativas e '
                        f'{format((time.time() - start), ".0f")} segundos')

    def save_frame(self, filename: str):
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        ret, frame = self.read()
        if not ret:
            msg = "Unable to save frame, make sure the camera is working and connected."
            warnings.warn(msg)
        else:
            cv2.imwrite(filename, frame)

    def close(self):
        self._keep_running = False
        self._thread.join()


def get_rtsp_url(server: str, login: str, password: str, rtsp_port=554, channel=1, subtype=0) -> str:
    url = f'rtsp://{login}:{password}@{server}:{rtsp_port}' \
          f'/cam/realmonitor?channel={channel}&subtype={subtype}'
    return url


def graceful_handler(method: Callable):
    """
    Handles an exception gracefully, A.K.A. showing the user a pop-up window with the error
    for better debugging.
    """
    try:
        method()
    except KeyboardInterrupt:
        pass

    except Exception as e:
        showerror(title="Erro inesperado", message=str(e))
        logging.exception(e)


def try_camera_connection(source: str, timeout: float):
    succeeded = timed_out = False
    pool = multiprocessing.Pool(processes=1)
    async_obj = pool.apply_async(is_camera_working, (source,))

    try:
        succeeded = async_obj.get(timeout=timeout)

    except multiprocessing.TimeoutError:
        # Terminate the process if it times out
        if hasattr(async_obj, "terminate"):
            async_obj.terminate()
        else:
            pool.terminate()
        timed_out = True

    pool.close()
    pool.join()

    return succeeded, timed_out


def is_camera_working(src: str):
    result = False
    cap = cv2.VideoCapture(src)
    # Check if the camera opened successfully
    if cap.isOpened():
        result = True
        cap.release()  # Release the camera when done
    return result
