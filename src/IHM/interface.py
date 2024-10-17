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
    thread = None
    def __init__(self,product_json:list):
        if self.thread is None:
            self.__config_thread(product_json)

    def _run_interface(self):
        self.thread.start()

    def __config_thread(self,product_json):
        self.worker = self._run_ihm
        self.thread = Process(target=self.worker, args=[product_json])

    def _run_ihm(self,json_produts:list):
        app = QApplication()
        controller_view = ControllerView(json_produts)
        controller_view.show()
        app.exec()
