import time

from src.IHM.src.components.inspection_return.inspection_return import InspectionReturn
from src.IHM.src.components.inspection_video.inspection_video import InspectionVideo
from src.IHM.src.components.video_preview.video_preview import VideoPreview
import queue

from src.IHM.src.view.second_screen.second_screen_ui import Ui_Form
from src.IHM.src.view.second_screen.ui_second_screen import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
from PySide6.QtCore import QTimer, Signal

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult


class SecondScreen(QWidget, Ui_Form):
    OpenFirstScreen = Signal()
    OnClose = Signal()

    def __init__(self):
        super(SecondScreen, self).__init__()
        self.setupUi(self)
        self.placard_style_list = ["background-color: rgb(13, 116, 18);\ncolor: rgb(255, 255, 255);","color: rgb(0, 0, 0);\nbackground-color: rgb(53, 132, 228);"]
        self.__config_components()
        self.__config_video()
        self.set_time_placards()
        self.confing_history()
        self.showFullScreen()
        self.setVisible(False)

    def __config_components(self):
        self.timer_result = QTimer()
        # self.inspection_result_plate = InspectionReturn(self)
        # self.video_place.layout().addWidget(self.inspection_result_plate)
        self.__reset_results_on_screen()
        self.timer_result.timeout.connect(self.__reset_results_on_screen)
        self.button_to_model_screen.clicked.connect(self.to_first_screen)

    def __reset_results_on_screen(self):
        # self.approved_product.setVisible(False)
        # self.rejected_product.setVisible(False)
        pass

    def to_first_screen(self):
        self.setVisible(False)
        self.clean_history()
        self.OpenFirstScreen.emit()

    def get_on_inspection_functions(self) -> list:
        response_methods = [self.enum_to_history, self.mostrar_aprovado_reprovado]
        return response_methods

    def __config_video(self):
        self.video = InspectionVideo(self.video_place)
        self.video_place.layout().addWidget(self.video)
        self.video.start_video()
    def change_placard(self): #Fazer a parte do inspection com o Enum
        self.label_placard.setStyleSheet(self.placard_style_list[int(self.show_placard)])
        self.label_placard.setText("INSPEÇÃO TAMPOGRAFIA SWITCH 8p" if self.show_placard else "EQUIPE AUTOMAÇÃO - INTELBRAS")
        self.show_placard = not self.show_placard

    def set_name_switch(self, name_switch):
        self.model_label.setText(f'{name_switch}')

    def get_name_switch(self):
        return self.model_label.text()

    def set_time_placards(self):
        self.time = QTimer()
        self.time.timeout.connect(self.change_placard)
        self.time.start(3000)
        self.show_placard = True

    def enum_to_history(self, result):
        if self.is_history_full() and result == InspectionResult.NOVO_CICLO:
            self.clean_history()
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
        self.queue_hisory.put(self.label_hist_one)
        self.queue_hisory.put(self.label_hist_two)

    def clean_history(self):
        for _ in range(0,self.queue_hisory.qsize()):
            obj = self.queue_hisory.get()
            obj.setText("INSPECIONANDO...")
            obj.setStyleSheet("background-color: yellow")
        self.confing_history()

    def is_history_full(self) -> bool:
        if self.label_hist_one.text() != "INSPECIONANDO..." and self.label_hist_two.text() != "INSPECIONANDO...":
            return True
        return False






    def mostrar_aprovado_reprovado(self, resultado: InspectionResult):
        if resultado == InspectionResult.APROVADO:
            self.video.approved_plate()

        elif resultado == InspectionResult.REPROVADO:
            self.video.repproved_plate()

        self.timer_result.start(3000)

    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
