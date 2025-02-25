from multiprocessing import Process
from PySide6.QtWidgets import QApplication
from src.IHM.src.view.controller_view.controller_view import ControllerView

class Interface:
    _thread = None

    def __init__(self):
        if self._thread is None:
            self.__config_thread()

    def _run_interface(self):
        self._thread.start()

    def __config_thread(self):
        self._worker = self._run_ihm
        self._thread = Process(target=self._worker)
    @staticmethod
    def _run_ihm():
        app = QApplication()
        controller_view = ControllerView()
        controller_view.show()
        app.exec()
