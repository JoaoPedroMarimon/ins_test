import time

from PySide6.QtGui import QFont

from src.IHM.src.components.history.history import History
from src.IHM.src.components.inspection_return.inspection_return import InspectionReturn
from src.IHM.src.components.inspection_video.inspection_video import InspectionVideo
from src.IHM.src.components.video_preview.video_preview import VideoPreview
import queue

from src.IHM.src.view.second_screen.second_screen_ui import Ui_Form
from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
from PySide6.QtCore import QTimer, Signal

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.utils import map_value


class SecondScreen(QWidget, Ui_Form):
    OpenFirstScreen = Signal()
    OnClose = Signal()

    def __init__(self):
        super(SecondScreen, self).__init__()
        self.history = None
        self.setupUi(self)
        self.__config_components()
        self.showFullScreen()
        self.setVisible(False)

    def __config_components(self):
        self.clean_placard()
        self._confing_history()
        self.__config_video()
        self.button_to_model_screen.clicked.connect(self.to_first_screen)

    def _confing_history(self):
        self.history = History(self.hist_container)
        self.hist_container.layout().addWidget(self.history)


    def __config_video(self):
        self.video = InspectionVideo(self.video_place)
        self.video_place.layout().addWidget(self.video)

    def to_first_screen(self):
        self.setVisible(False)
        self.history.clean_history()
        self.OpenFirstScreen.emit()

    def set_markers_on_placard(self, position:str, markers_list):
        if markers_list is not None and len(markers_list) != 0:
            new_font = self.label_placard.font()
            font_size = map_value(len(markers_list),1,50,self.label_placard.size().height()/8,16)
            new_font.setPixelSize(font_size)
            self.label_placard.setFont(new_font)

            markers_name = [makers["name"] for makers in markers_list]
            markers_name = ", ".join(markers_name)
            if self.label_placard.text() == "EQUIPE AUTOMAÇÃO - INTELBRAS":
                self.label_placard.setText(f"{position}: {markers_name}\n\n")
            else:
                self.label_placard.setText(f"{self.label_placard.text()}{position}: {markers_name}")

    def clean_placard(self):
            new_font = self.label_placard.font()
            new_font.setPointSize(23)
            self.label_placard.setFont(new_font)
            self.label_placard.setText("EQUIPE AUTOMAÇÃO - INTELBRAS")

    def set_name_switch(self, name_switch):
        self.model_label.setText(f'{name_switch}')

    def get_name_switch(self):
        return self.model_label.text()


    def show_inspection_result(self, position,resultado: InspectionResult):
        if resultado == InspectionResult.APROVADO:
            self.video.approved_plate()

        elif resultado == InspectionResult.REPROVADO:
            self.video.reproved_plate()


    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
