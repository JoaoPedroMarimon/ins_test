from src.IHM.src.components.video_preview.video_preview import VideoPreview
import queue
from src.IHM.src.view.second_screen.ui_second_screen import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QVBoxLayout)
from PySide6.QtCore import QTimer, Signal

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult


class SecondScreen(QMainWindow, Ui_MainWindow):
    OpenFirstScreen = Signal()
    OnClose = Signal()

    def __init__(self):
        super(SecondScreen, self).__init__()
        self.setupUi(self)
        self.__config_video()
        self.__config_components()
        self.set_time_placards()
        self.confing_history()


    def __config_components(self):
        self.timer_result = QTimer()
        self.timer_result.timeout.connect(self.__reset_results_on_screen)
        self.__reset_results_on_screen()
        self.back_to_firstscreen.clicked.connect(self.to_first_screen)

    def __reset_results_on_screen(self):
        self.approved_product.setVisible(False)
        self.rejected_product.setVisible(False)

    def to_first_screen(self):
        self.setVisible(False)
        self.OpenFirstScreen.emit()

    def get_on_response_functions(self) -> list:
        response_methods = [self.enum_to_history, self.mostrar_aprovado_reprovado]
        return response_methods

    def __config_video(self):
        self.video = VideoPreview(self.label)
        self.video.onVideonotOpened.connect(lambda: print("deu ruim"))
        self.video.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setLayout(QVBoxLayout())
        self.label.layout().addWidget(self.video)
        self.video.start_video()

    def change_placard(self): #Fazer a parte do inspection com o Enum
        if self.show_placard:
            self.placard_team.setVisible(True)
            self.placard_jiga.setVisible(False)
        else:
            self.placard_team.setVisible(False)
            self.placard_jiga.setVisible(True)

        self.show_placard = not self.show_placard

    def set_name_switch(self, name_switch):
        self.switch_model.setText(f'{name_switch}')

    def get_name_switch(self):
        return self.switch_model.text()

    def set_time_placards(self):
        self.time = QTimer()
        self.time.timeout.connect(self.change_placard)
        self.time.start(3000)
        self.show_placard = True

    def enum_to_history(self, result):
        if result == InspectionResult.APROVADO:
            obj = self.queue_hisory.get()
            obj.setText('APROVADO')
            obj.setStyleSheet("background-color: #00A336; color: white;")
            self.queue_hisory.put(obj)  # Coloca o objeto de volta na fila

        elif result == InspectionResult.REPROVADO:
            obj = self.queue_hisory.get()
            obj.setText('REPROVADO')
            obj.setStyleSheet("background-color: #ff0000; color: white;")
            self.queue_hisory.put(obj)  # Coloca o objeto de volta na fila

        else:
            obj = self.queue_hisory.get()
            obj.setText("INSPECIONANDO...")
            obj.setStyleSheet("background-color: yellow")



    def confing_history(self):
        self.queue_hisory = queue.Queue()
        self.queue_hisory.put(self.label_product_one)
        self.queue_hisory.put(self.label_product_two)
        self.queue_hisory.put(self.label_product_three)


    def mostrar_aprovado_reprovado(self, resultado: InspectionResult):
        if resultado == InspectionResult.APROVADO:
            self.approved_product.setVisible(True)

        elif resultado == InspectionResult.REPROVADO:
            self.rejected_product.setVisible(True)

        self.timer_result.start(3000)

    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
