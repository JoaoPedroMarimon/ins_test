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
        self.queue_history = None
        self.__config_components()
        self.showFullScreen()
        self.setVisible(False)

    def __config_components(self):
        self.button_to_model_screen.clicked.connect(self.to_first_screen)
        self.confing_history()
        self.__config_video()


    def to_first_screen(self):
        self.setVisible(False)
        self.clean_history()
        self.OpenFirstScreen.emit()


    def confing_history(self):
        if self.queue_history is None:
            self.queue_history = queue.Queue()
        self.queue_history.put(self.label_hist_one)
        self.queue_history.put(self.label_hist_two)

    def __config_video(self):
        self.video = InspectionVideo(self.video_place)
        self.video_place.layout().addWidget(self.video)

    def set_markers_on_placard(self,markers_list):
        if markers_list is not None:
            print(markers_list)
            markers_name = [makers["name"] for makers in markers_list["markers"]]
            markers_name = ", ".join(markers_name)
            self.label_placard.setText(markers_name)

    def clean_placard(self, result):
        if result is InspectionResult.APROVADO or result is InspectionResult.NOVO_CICLO:
            self.label_placard.setText("EQUIPE AUTOMAÇÃO - INTELBRAS")

    def set_name_switch(self, name_switch):
        self.model_label.setText(f'{name_switch}')

    def get_name_switch(self):
        return self.model_label.text()

    def enum_to_history(self, result):
        if self.is_history_full() and InspectionResult.NOVO_CICLO:
            self.clean_history()
        if result == InspectionResult.APROVADO:
            obj = self.queue_history.get()
            obj.setText('APROVADO')
            obj.setStyleSheet("background-color: #00A336; color: white;")
            self.queue_history.put(obj)  # Coloca o objeto de volta na fila

        elif result == InspectionResult.REPROVADO:
            obj = self.queue_history.get()
            obj.setText('REPROVADO')
            obj.setStyleSheet("background-color: #ff0000; color: white;")
            self.queue_history.put(obj)  # Coloca o objeto de volta na fila




    def clean_history(self):
        for _ in range(0, self.queue_history.qsize()):
            obj = self.queue_history.get()
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


    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
