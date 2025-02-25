from abc import ABC, abstractmethod

from ..packet.packet import Packet, PacketType
from ..packet.utils import validate_dict_packet, dict_packet_to_struct_packet_bytes, PACKET_LENGTH, get_packet_length,BASE_PACKET_SCHEMA


class BaseIPC(ABC):
    def __init__(self, address: str, packet_schema=BASE_PACKET_SCHEMA):
        self._address = address
        self._packet_schema = packet_schema

    @property
    def address(self):
        return self._address

    @property
    def packet_schema(self):
        return self._packet_schema

    @packet_schema.setter
    def packet_schema(self, schema):
        self._packet_schema = schema

    @abstractmethod
    def _handle_packets(self):
        pass

    @abstractmethod
    def _send_packet(self, packet: Packet):
        pass

    @abstractmethod
    def _read_packet(self) -> Packet | None:
        """
        Reads a packet from the socket and returns it as a `Packet` object, or `None` if no data is available.
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    def notify(self, message: str, body: dict = None):
        packet = Packet("", PacketType.NOTIFICATION, message, body or {})
        self._send_packet(packet)

    def request(self, packet_id: str, message: str, body: dict = None):
        packet = Packet(packet_id, PacketType.REQUEST, message, body or {})
        self._send_packet(packet)

    def respond(self, packet_id: str, message: str, body: dict = None):
        packet = Packet(packet_id, PacketType.RESPONSE, message, body or {})
        self._send_packet(packet)

    def create_valid_struct_bytes_packet(self, packet: Packet) -> bytes:
        dict_packet = packet.as_dict()
        validate_dict_packet(dict_packet, self._packet_schema)
        return dict_packet_to_struct_packet_bytes(dict_packet)
