import os
import socket
import queue
from threading import Thread
from src.utils import PACKET_LENGTH

class HMIReceiver:
    def __init__(self):
        self._server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._packet_queue = queue.Queue()
        self.config_server()
        self._client = None
        self.start()
    def config_server(self):
        if os.path.exists("/tmp/IHM"):
            os.remove("/tmp/IHM")
        self._server.bind("/tmp/IHM")
        self._server.listen(5)

    def start(self):
        self._handler_thread = Thread(target=self._handle_packets, daemon=True)
        self._handler_thread.start()

    def _wait_client(self):
        try:
            client, address = self._server.accept()
            return client, address
        except socket.error:
            return None, ""

    def _handle_packets(self):
        self._client, _ = self._wait_client()
        print(f"O cliente {self._client} esta conectado em {_}")
        if self._client is not None:
            try:
                while True:
                    packet = self._read_packet()
                    if not packet:
                        break
                    self._packet_queue.put(packet)
            finally:
                self._client.close()
                self._client = None

    def has_packets(self):
        return not self._packet_queue.empty()

    def _read_packet(self):
        packet_struct_length = self._client.recv(PACKET_LENGTH)
        if not packet_struct_length:
            return None  # No data to read
        # Read the packet data and convert it into a Packet object
        packet_length = int.from_bytes(packet_struct_length, byteorder='big')
        packet = self._client.recv(packet_length)
        if not packet:
            return None
        return packet



