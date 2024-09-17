from multiprocessing import Process
from PySide6.QtWidgets import QApplication
import threading
import time

from src.IHM.src.view.controller_view.controller_view import ControllerView
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Interface(Singleton):
    _thread = None
    _client = None

    def __init__(self):
        if self._thread is None:
            self.__config_thread()
            self.run_interface()

    def __config_thread(self):
        self.worker = self._run_ihm
        self._thread = Process(target=self.worker)

    def run_interface(self):
        self._thread.start()

    def is_alive(self) -> bool:
        if self._thread is None:
            return False
        return self._thread.is_alive()

    def _run_ihm(self):
        app = QApplication()
        self.controller_view = ControllerView()
        self.controller_view.show()
        app.exec()

    def get_model(self) -> str:
        return self.controller_view.second_screen.switch_model.text()


if __name__ == "__main__":
    print("iniciou")
    inter = Interface()
    time.sleep(4)
    while True:
        time.sleep(8)
    # print("1 is alive - " + str(inter.is_alive()))
