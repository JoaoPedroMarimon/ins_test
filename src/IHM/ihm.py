from hmi_receiver import HMIReceiver
from .interface import Interface


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class IHM(Singleton,Interface):
    def __init__(self, products_list: list):
        super().__init__(products_list)
        self._server = HMIReceiver()

    def run_ihm(self):
        super()._run_interface()

    def is_alive(self):
        if self.thread is None:
            return False
        return self.thread.is_alive()

    def get_model_index(self) -> int | None:
        return self._server.get_model_index()

