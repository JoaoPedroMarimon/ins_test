import sys
import time

from src.IHM.src.client.client import Client

RESULT_ADRESS = "result-"
ORDER_ADRESS = "order-"


class HMIClient(Client):
    def __init__(self):
        if sys.platform == "linux":
            super().__init__("/tmp/IHM")
        else:
            super().__init__(("127.0.0.1", 1111))

        self.connect()

    def send_approved(self) -> None:
        if self._client is None:
            print("Não há conexão com o IHM")
            return
        self.send_packet(bytes(RESULT_ADRESS + "aprovado", "utf-8"))

    def send_reproved(self) -> None:
        if self._client is None:
            print("Não há conexão com o IHM")
            return
        self.send_packet(bytes(RESULT_ADRESS + "reprovado", "utf-8"))

    def get_model(self) -> str | None:
        if self._client is None:
            print("Não há conexão com o IHM")
            return
        self.send_packet(bytes(ORDER_ADRESS + "model", "utf-8"))
        response = self._client.recv(90)
        return response

    def wait_receiving_model(self) -> str:
        while True:
            response = self.get_model()
            if response != b'MODELO SWITCH':
                return response
            time.sleep(0.3)
