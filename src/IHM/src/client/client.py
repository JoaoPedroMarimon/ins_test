import socket
import sys
import time


class Client:
    def __init__(self, server_name: tuple[str, int] | str):
        system = sys.platform
        self._server_name = server_name
        if system == "linux":
            self._client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        else:
            self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._is_connected = False

    def connect(self):
        if not self.is_connected():
            try:
                self._client.connect(self._server_name)
            except FileNotFoundError:
                print("conexão falhou... reconectando")
                time.sleep(2)
                self.connect()
            self._is_connected = True
            print("conexão foi um sucesso")

    def is_connected(self):
        return self._is_connected

    def send_packet(self, packet_bytes_data: bytes):
        try:
            print("mandando pacotes")
            self._client.sendall(packet_bytes_data)
        except socket.error:
            self._is_connected = False


