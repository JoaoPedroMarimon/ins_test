from abc import ABC
from threading import Thread

import numpy as np
from numpy.random.mtrand import Sequence

from src.IHM.src.components.communication.interfaces.ipc_server import IPCServer
from src.IHM.src.components.communication.packet.utils import BASE_PACKET_SCHEMA
from src.IHM.src.components.communication.packet.packet import Packet, PacketType
from src.utils import PACKET_LENGTH


class HMIReceiver(IPCServer):
    def __init__(self):
        super().__init__("/tmp/IHM",packet_schema=BASE_PACKET_SCHEMA)
        self._receive_packet_handler_thread = None
        self._ihm_status: dict= {
            'model': None,
            'button': False,
            'close': False
        }

    def packet_receiver(self):
        while True:
            packet = self.get_packet()
            match packet.message:
                case 'get_model':
                    self._ihm_status.update(packet.body)
                case "button_continue":
                    self._ihm_status["button"] = packet.body['status']
                case "alert_close":
                    self._ihm_status["close"] = packet.body["close"]
    def send_approved(self,position: str) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,"inspection", {"position": position ,"result":"approved"}))

    def send_reproved(self,position: str) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,"inspection", {"position": position,"result":"reproved"}))

    def send_markers(self,position:str,markers):
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

    def get_alert_close(self) -> bool:
        return self._ihm_status['close']

    def open_limit_exceed_screen(self):
        self._send_packet(Packet("0", PacketType.REQUEST, "limit_exceed", {}))

    def __open_alert_screen(self,reason:str):
        self._send_packet(Packet("0",PacketType.REQUEST,"alert_screen",{"reason":reason}))

    def open_alert_screen_camera(self):
        self.__open_alert_screen("camera")

    def open_alert_screen_arduino(self):
        self.__open_alert_screen("arduino")

    def start(self):
        super().start()
        self._receive_packet_handler_thread = Thread(target=self.packet_receiver,daemon=True)
        self._receive_packet_handler_thread.start()

