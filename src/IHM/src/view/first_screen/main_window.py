from src.IHM.src.view.first_screen.main_window_ui import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from PySide6.QtCore import Slot, Signal


class MainWindow(QMainWindow, Ui_MainWindow):
    modelSig = Signal(str)
    OpenSecondScreen = Signal()
    OnClose = Signal()
    def __init__(self, product_json:dict):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Executa uma função lambda(anônima) em linha, fazendo com que chame a função de mostrar a tela passando o modelo
        self.button_model_sf800.setText(product_json[0]['name'])
        self.button_model_sg800.setText(product_json[1]['name'])
        self.button_model_s1108f.setText(product_json[2]['name'])
        self.button_model_s1108g.setText("Sobra")
        self.button_model_sf800.clicked.connect(lambda: self.set_model_switch(product_json[0]['name']))
        self.button_model_sg800.clicked.connect(lambda: self.set_model_switch(product_json[1]['name']))
        self.button_model_s1108f.clicked.connect(lambda: self.set_model_switch(product_json[2]['name']))
        self.button_model_s1108g.clicked.connect(lambda: self.set_model_switch("Sobra"))

    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()

    def to_second_screen(self):
        self.setVisible(False)
        self.OpenSecondScreen.emit()

    def set_model_switch(self, model_name):
        self.modelSig.emit(model_name)
        self.to_second_screen()
        """
        # Aqui ficaria responsável pela conexão com o arduino, mandando o sinal de qual dos modelos de switch foi escolhido.
        # por exemplo: print("O modelo A foi escolhido!")
        #
        # E logo abaixo daria continuação ao código, executando segunda tela com o video
        """
