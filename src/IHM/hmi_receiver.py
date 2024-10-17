from abc import ABC
from threading import Thread
from src.IHM.src.components.communication.interfaces.ipc_server import IPCServer
from src.IHM.src.components.communication.packet.utils import BASE_PACKET_SCHEMA
from src.utils import PACKET_LENGTH


class HMIReceiver(IPCServer, ABC):
    def __init__(self):
        super().__init__("/tmp/IHM",packet_schema=BASE_PACKET_SCHEMA)
        self._receive_packet_handler_thread = None
        self._ihm_status = {
            'model': None
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
                case "model":
                    self._ihm_status["model"] = packet.body['model']
                    break

    def get_model_index(self) -> int | None:
        return self._ihm_status['model']
    def start(self):
        super().start()
        self._receive_packet_handler_thread = Thread(target=self.packet_receiver,daemon=True)
        self._receive_packet_handler_thread.start()




