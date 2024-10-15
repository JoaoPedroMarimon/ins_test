from PySide6.QtCore import QObject

from src.IHM.src.view.first_screen.main_window import MainWindow
from src.IHM.src.view.second_screen.second_screen import SecondScreen
from src.IHM.src.components.communication.ihm_client import IHMClient


class ControllerView(QObject):
    def __init__(self,product_json:dict):
        super().__init__()
        self.__product_json = product_json
        self.first_screen = MainWindow(product_json=product_json)
        self.second_screen = SecondScreen()
        self.__config_server()
        self.signals_first_screen()
        self.signals_second_screen()

    def __config_server(self):
        self._server = IHMClient()
        self._server.OnReceiveResult.connect(self.second_screen.enum_to_history)
        self._server.OnReceiveResult.connect(self.second_screen.mostrar_aprovado_reprovado)



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
        self._server.send_model_index(self.get_model_index())

    def get_model_index(self) -> int | None:
        model_name = self.get_switch_model()
        if model_name == 'MODELO SWITCH':
            return None
        return list(self.__product_json.keys()).index(model_name)

    def get_switch_model(self) -> str:
        return self.second_screen.get_name_switch()


    def on_close(self) -> None:
        self.first_screen.close()
        self.second_screen.close()
        self._server.close()
