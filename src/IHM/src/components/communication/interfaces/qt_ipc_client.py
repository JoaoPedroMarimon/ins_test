from abc import ABC, abstractmethod

from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QLocalSocket

from .base_ipc import BaseIPC
from ..packet.packet import Packet
from ..packet.utils import packet_from_bytes, get_packet_length, PACKET_LENGTH


class _QtBaseIPC(BaseIPC, ABC):
    def __init__(self, address: str, packet_schema: dict, parent):
        super().__init__(address, packet_schema)
        self.socket = QLocalSocket(parent)

    def _handle_packets(self):
        try:
            while self.socket.bytesAvailable() > 0:
                packet = self._read_packet()
                if not packet:
                    continue
                self._on_packet_received(packet)

        except Exception as e:
            self._on_unexpected_error(e)

    def _read_packet(self) -> Packet | None:
        packet_struct_length = self.socket.read(PACKET_LENGTH)
        if not packet_struct_length:
            return  # No data to read
        length = get_packet_length(packet_struct_length)
        # Read the packet data and convert it into a Packet object
        packet = packet_from_bytes(self.socket.read(length).data())
        return packet

    def _send_packet(self, packet: Packet):
        if self.is_connected():
            bytes_packet = self.create_valid_struct_bytes_packet(packet)
            self.socket.write(bytes_packet)

    @abstractmethod
    def _on_packet_received(self, packet: Packet):
        pass

    @abstractmethod
    def _on_unexpected_error(self, e):
        pass

    def start(self):
        self.socket.readyRead.connect(self._handle_packets)
        self.socket.connectToServer(self._address)

    def is_connected(self):
        return self.socket.state() == QLocalSocket.LocalSocketState.ConnectedState


class QtIPCMeta(type(QObject), type(_QtBaseIPC)):
    pass


class QtIPCClient(_QtBaseIPC, ABC, QObject, metaclass=QtIPCMeta):
    packetReceivedSig = Signal(Packet)

    def __init__(self, address, packet_schema, parent=None) -> None:
        QObject.__init__(self, parent)
        _QtBaseIPC.__init__(self, address, packet_schema, self)

    def _on_packet_received(self, packet: Packet):
        self.packetReceivedSig.emit(packet)
