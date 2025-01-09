from abc import ABC
from threading import Thread

import numpy as np
from numpy.random.mtrand import Sequence

from src.IHM.src.components.communication.interfaces.ipc_server import IPCServer
from src.IHM.src.components.communication.packet.utils import BASE_PACKET_SCHEMA
from src.IHM.src.components.communication.packet.packet import Packet, PacketType
from src.utils import PACKET_LENGTH


class HMIReceiver(IPCServer, ABC):
    def __init__(self):
        super().__init__("/tmp/IHM",packet_schema=BASE_PACKET_SCHEMA)
        self._receive_packet_handler_thread = None
        self._ihm_status: dict= {
            'model': None,
            'button': False
        }
    # def _read_packet(self):
    #     packet_struct_length = self._client.recv(PACKET_LENGTH)
    #     if not packet_struct_length:
    #         return None  # No data to read
    #     # Read the packet data and convert it into a Packet object
    #     packet_length = int.from_bytes(packet_struct_length, byteorder='big')
    #     packet = self._client.recv(packet_length)
    #     if not packet:
    #         return None
    #     return packet

    def packet_receiver(self):
        while True:
            packet = self.get_packet()
            print(f"packet {packet.message} received!!!\n whith the message: {packet.body} ")
            match packet.message:
                case 'get_model':
                    self._ihm_status.update(packet.body)
                case "button_continue":
                    self._ihm_status["button"] = packet.body['status']
    def send_approved(self,position: str) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,"inspection", {"position": position ,"result":"approved"}))

    def send_reproved(self,position: str) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,"inspection", {"position": position,"result":"reproved"}))

    def send_inspect_frame(self,position:str,markers):
        self._send_packet(Packet("0",PacketType.REQUEST,"frame_inspection",{"position":position,"markers": markers}))

    def new_cycle(self) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,"new_cycle",{}))

    def get_model_index(self) -> int | None:
        return self._ihm_status['model']

    def get_status_button_continue(self) -> bool:
        if self._ihm_status['button'] is True:
            self._ihm_status.update({'button': False})
            return True
        return self._ihm_status.get('button',False)

    def open_limit_exceed_screen(self):
        self._send_packet(Packet("0", PacketType.REQUEST, "limit_exceed", {}))

    def start(self):
        super().start()
        self._receive_packet_handler_thread = Thread(target=self.packet_receiver,daemon=True)
        self._receive_packet_handler_thread.start()

