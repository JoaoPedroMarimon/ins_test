from multiprocessing import Process
from PySide6.QtWidgets import QApplication
import time

from src.IHM.src.view.controller_view.controller_view import ControllerView
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Interface:
    _thread = None
    _client = None

    def __init__(self,product_json:list):
        if self._thread is None:
            self.__config_thread(product_json)

    def run_interface(self):
        self._thread.start()

    def __config_thread(self,product_json):
        self.worker = self._run_ihm
        self._thread = Process(target=self.worker,args=[product_json])

    def _run_ihm(self,json_produts:list):
        app = QApplication()
        controller_view = ControllerView(json_produts)
        controller_view.show()
        app.exec()

    def is_alive(self) -> bool:
        if self._thread is None:
            return False
        return self._thread.is_alive()


if __name__ == "__main__":
    print("iniciou")
    inter = Interface()
    while True:
        time.sleep(1)
        print("1 is alive - " + str(inter.is_alive()))
