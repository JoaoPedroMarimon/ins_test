import os
import socket
import queue
from abc import abstractmethod
from threading import Thread

from .base_ipc import BaseIPC
from ..packet.packet import Packet
from ..packet.utils import packet_from_bytes, get_packet_length, PACKET_LENGTH


class IPCServer(BaseIPC):
    def __init__(self, address: str, packet_schema: dict):
        super().__init__(address, packet_schema)
        os.path.exists(address) and os.remove(address)
        self._server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._server.bind(address)
        self._server.listen(5)

        self._client = None

        self._packet_queue = queue.Queue()
        self._packet_handler_thread = None
        self.start()

    def _wait_client(self):
        try:
            client, address = self._server.accept()
            return client, address

        except socket.error:
            return None, ""

    def _handle_packets(self):
        self._client, _ = self._wait_client()
        if self._client is not None:
            try:
                while 1:
                    packet = self._read_packet()
                    if not packet:
                        break
                    self._packet_queue.put(packet)
            finally:
                self._client.close()
                self._client = None

    def _read_packet(self) -> Packet | None:
        packet_struct_length = self._client.recv(PACKET_LENGTH)
        if not packet_struct_length:
            return None  # No data to read
        # Read the packet data and convert it into a Packet object
        length = get_packet_length(packet_struct_length)
        packet = packet_from_bytes(self._client.recv(length))
        return packet

    def _send_packet(self, packet: Packet):
        if self._client is None:
            msg = "No client connected to server, unable to send packet."
            raise ConnectionError(msg)

        bytes_packet = self.create_valid_struct_bytes_packet(packet)
        self._client.sendall(bytes_packet)

    @abstractmethod
    def packet_receiver(self):
        pass

    def start(self):
        if self._client is None:
            self._packet_handler_thread = Thread(target=self._handle_packets, daemon=True)
            self._packet_handler_thread.start()

    def stop(self):
        self._client is not None and self._client.close()

    def close(self):
        self.stop()
        self._server.close()

    def is_connected(self):
        return self._client is not None

    def has_packets(self):
        return not self._packet_queue.empty()

    def get_packet(self, block=True, timeout: float = None) -> Packet:
        return self._packet_queue.get(block, timeout)
