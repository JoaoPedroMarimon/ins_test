from abc import ABC
from typing import Dict, Callable, Any

import numpy as np
from PySide6.QtCore import QObject, Signal
from src.IHM.src.components.communication.interfaces.qt_ipc_client import QtIPCClient
from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.IHM.src.components.communication.packet.packet import Packet
from src.IHM.src.components.communication.packet.packet import PacketType
from src.IHM.src.components.communication.packet.utils import BASE_PACKET_SCHEMA


class IHMClient(QtIPCClient, ABC):
    OnReceiveResult = Signal(InspectionResult)
    OpenLimitExceed = Signal()
    OnReceiveFrame = Signal(dict)
    OnNewCicle = Signal()
    def __init__(self):
        super().__init__(address="/tmp/IHM",packet_schema=BASE_PACKET_SCHEMA)
        self.packetReceivedSig.connect(self.react_packet)
        super().start()

    def _on_unexpected_error(self, e):
        print(e)


    def send_status_button_continue(self, status: bool) -> None:
        self._send_packet(Packet("1",PacketType.REQUEST,"button_continue", {"status": status}))

    def send_model_index(self, model: int) -> None:
        self._send_packet(Packet("0",PacketType.REQUEST,message="get_model", body={"model":model}))

    def react_packet(self, packet: Packet) -> None:
        match packet.message:
            case "inspection":
                self.OnReceiveResult.emit(InspectionResult.convert_to_enum(packet.body["result"]))
            case "limit_exceed":
                self.OpenLimitExceed.emit()
            case "frame_inspection":
                self.OnReceiveFrame.emit(packet.body)
            case "new_cycle":
                self.OnNewCicle.emit()


    def close(self):
        self.socket.close()
