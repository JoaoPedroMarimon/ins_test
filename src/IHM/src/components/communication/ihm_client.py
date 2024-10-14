import sys
from abc import ABC
from pathlib import Path

from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QLocalServer, QHostAddress, QTcpServer, QLocalSocket
from src.IHM.src.components.communication.interfaces.qt_ipc_client import QtIPCClient
from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.IHM.src.components.communication.packet.packet import Packet
from src.IHM.src.components.communication.packet.packet import PacketType
from src.IHM.src.components.communication.packet.utils import BASE_PACKET_SCHEMA


class IHMClient(QtIPCClient, ABC):
    OnReceiveResult = Signal(InspectionResult)

    def __init__(self):
        super().__init__(address="/tmp/IHM",packet_schema=BASE_PACKET_SCHEMA)
        super().start()

    def send_model(self, model: str):
        self._send_packet(Packet("0",PacketType.REQUEST,"get_model", {"model":model}))

    def close(self):
        self.socket.close()
