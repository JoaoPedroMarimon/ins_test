import dataclasses
from typing import Sequence

import numpy as np
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QSizePolicy

from src.IHM.src.components.inspection_return.inspection_return import InspectionReturn
from src.IHM.src.components.video_preview.video_preview import VideoPreview

class InspectionVideo(
    QWidget
):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self._video_preview = VideoPreview(parent)
        self._inspection_result_plate = InspectionReturn(parent)
        self._config_video()
        self._config_plate()


    def _config_video(self):
        self._video_preview.onVideonotOpened.connect(lambda: print("O vídeo não pode ser carregado"))
        self._video_preview.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.start_video()

    def _config_plate(self):
        self._inspection_result_plate.setGeometry(0, self.height()//2, self.width(), 80)

    def start_video(self):
        self._video_preview.start_video()

    def approved_plate(self):
        self._inspection_result_plate.approved()
    def reproved_plate(self):
        self._inspection_result_plate.reproved()



    def resizeEvent(self, event):
        self._config_plate()
        super().resizeEvent(event)


