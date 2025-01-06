from functools import partial

from src.IHM.src.view.first_screen.main_window_ui import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from PySide6.QtCore import Slot, Signal


class MainWindow(QMainWindow, Ui_MainWindow):
    modelSig = Signal(str)
    OpenSecondScreen = Signal()
    OnClose = Signal()
    def __init__(self, product_json):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        button_list = [self.button_model_a_2,self.button_model_b_2,self.button_model_c_2,self.button_model_d_2]
        index = 0
        for index, product in enumerate(product_json):
            button_list[index].setText(product['name'])
            button_list[index].clicked.connect(partial(self.set_model_switch,product['name']))
        button_list = button_list[index+1:]
        for button in button_list:
            button.setVisible(False)


    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()

    def to_second_screen(self):
        self.setVisible(False)
        self.OpenSecondScreen.emit()

    def set_model_switch(self, model_name: str) -> None:
        self.modelSig.emit(model_name)
        self.to_second_screen()
        """
        # Aqui ficaria responsável pela conexão com o arduino, mandando o sinal de qual dos modelos de switch foi escolhido.
        # por exemplo: print("O modelo A foi escolhido!")
        #
        # E logo abaixo daria continuação ao código, executando segunda tela com o video
        """
