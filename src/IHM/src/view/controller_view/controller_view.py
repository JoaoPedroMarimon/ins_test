from PySide6.QtCore import QObject

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.IHM.src.view.first_screen.main_window import MainWindow
from src.IHM.src.view.second_screen.second_screen import SecondScreen
from src.IHM.src.components.communication.ihm_server import IHMServer
from src.IHM.src.components.communication.controller_order import ControllerOrder
from src.IHM.src.components.communication.Enum.Inspection_order import InspectionOrder


class ControllerView(QObject):
    def __init__(self):
        super().__init__()
        self.first_screen = MainWindow()
        self.second_screen = SecondScreen()
        self.__config_server()
        self.signals_first_screen()
        self.signals_second_screen()

    def __config_server(self):
        self._server = IHMServer()
        self._server.add_order_functions(self.get_switch_model, InspectionOrder.GET_MODEL)
        for method in self.get_all_response_function_from_childs():
            self._server.add_order_functions(method,InspectionResult.APROVADO)

    def show(self):
        self.first_screen.show()

    def signals_first_screen(self) -> None:
        self.first_screen.modelSig.connect(self.switch_model_to_second_screen)
        self.first_screen.OpenSecondScreen.connect(self.open_second_screen)
        self.first_screen.OnClose.connect(self.on_close)

    def signals_second_screen(self) -> None:
        self.second_screen.OpenFirstScreen.connect(self.open_first_screen)
        self.second_screen.OnClose.connect(self.on_close)

    def open_first_screen(self) -> None:
        self.first_screen.setVisible(True)

    def open_second_screen(self) -> None:
        self.second_screen.setVisible(True)

    def switch_model_to_second_screen(self, switch_model: str) -> None:
        self.second_screen.set_name_switch(switch_model)

    def get_switch_model(self) -> str:
        return self.second_screen.get_name_switch()

    def get_all_response_function_from_childs(self) -> list:
        list_fun = []
        list_fun += self.second_screen.get_on_response_functions()
        return list_fun
    def on_close(self) -> None:
        self.first_screen.close()
        self.second_screen.close()
        self._server.close()
