from typing import Sequence

import numpy as np

from src.IHM.hmi_receiver import HMIReceiver
from .interface import Interface
from .src.config import Config


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class IHM(Singleton, Interface):
    def __init__(self, config_json):
        super().__init__()
        self._server = HMIReceiver()
        Config(config_json)
    def run_ihm(self):
        super()._run_interface()

    def is_alive(self):
        if self._thread is None:
            return False
        return self._thread.is_alive()

    def get_model_index(self) -> int | None:
        return self._server.get_model_index()

    def get_status_button_continue(self):
        return self._server.get_status_button_continue()

    def open_limit_exceed_screen(self):
        self._server.open_limit_exceed_screen()

    def send_approved(self,position: str) -> None:
        self._server.send_approved(position)

    def send_reproved(self,position: str) -> None:
        self._server.send_reproved(position)

    def send_markers(self,position: str, markers):
        self._server.send_inspect_frame(position,markers)

    def new_cycle(self) -> None:
        self._server.new_cycle()
