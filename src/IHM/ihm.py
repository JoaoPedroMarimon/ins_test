from src.IHM.hmi_receiver import HMIReceiver
from .interface import Interface
from .src.config import Config


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class IHM(Singleton, Interface,HMIReceiver):
    def __init__(self, config_json):
        super().__init__()
        HMIReceiver.__init__(self)
        Config(config_json)
    def run_ihm(self):
        super()._run_interface()

    def is_alive(self):
        if self._thread is None:
            return False
        return self._thread.is_alive()


