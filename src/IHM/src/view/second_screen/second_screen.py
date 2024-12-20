import time

from src.IHM.src.components.history.history import History
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
        self.history = None
        self.setupUi(self)
        self.queue_history = None
        self.__config_components()
        self.showFullScreen()
        self.setVisible(False)

    def __config_components(self):
        self.confing_history()
        self.__config_video()
        self.button_to_model_screen.clicked.connect(self.to_first_screen)

    def confing_history(self):
        self.history = History(self.hist_container)
        self.hist_container.layout().addWidget(self.history)


    def __config_video(self):
        self.video = InspectionVideo(self.video_place)
        self.video_place.layout().addWidget(self.video)

    def to_first_screen(self):
        self.setVisible(False)
        self.history.clean_history()
        self.OpenFirstScreen.emit()

    def set_markers_on_placard(self,markers_list):
        if markers_list is not None:
            print(markers_list)
            markers_name = [makers["name"] for makers in markers_list["markers"]]
            markers_name = ", ".join(markers_name)
            self.label_placard.setText(markers_name)

    def clean_placard(self):
            self.label_placard.setText("EQUIPE AUTOMAÇÃO - INTELBRAS")

    def set_name_switch(self, name_switch):
        self.model_label.setText(f'{name_switch}')

    def get_name_switch(self):
        return self.model_label.text()

    # def enum_to_history(self, position: str,result: InspectionResult):
    #     if self.is_history_full():
    #         self.clean_history()
    #
    #     hist = self.queue_history.get()
    #     hist_position = hist[0]
    #     hist_position.setText(position)
    #     hist_result = hist[1]
    #     if result == InspectionResult.APROVADO:
    #         hist_result.setText('APROVADO')
    #         hist.setStyleSheet("background-color: #00A336; color: white;")
    #
    #
    #     elif result == InspectionResult.REPROVADO:
    #         hist_result.setText('REPROVADO')
    #         hist_result.setStyleSheet("background-color: #ff0000; color: white;")
    #         hist_position.setStyleSheet("background-color: #ff0000; color: white;")
    #
    #     self.queue_history.put(hist)  # Coloca o objeto de volta na fila
    #
    #
    # def clean_history(self):
    #     for _ in range(0, self.queue_history.qsize()):
    #         hist = self.queue_history.get()
    #         hist_position = hist[0]
    #         hist_position.setText("")
    #         hist_result = hist[1]
    #         hist_result.setText("INSPECIONANDO...")
    #         hist_result.setStyleSheet("background-color: yellow")
    #         hist_position.setStyleSheet("background-color: yellow")
    #     self.confing_history()
    #
    # def is_history_full(self) -> bool:
    #     if self.result.text() != "INSPECIONANDO..." and self.result_2.text() != "INSPECIONANDO...":
    #         return True
    #     return False


    def mostrar_aprovado_reprovado(self, resultado: InspectionResult):
        if resultado == InspectionResult.APROVADO:
            self.video.approved_plate()

        elif resultado == InspectionResult.REPROVADO:
            self.video.repproved_plate()


    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
