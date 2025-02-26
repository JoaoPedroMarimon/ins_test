import dataclasses
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QSizePolicy

from src.IHM.src.components.inspection_return.inspection_return_ui import Ui_inspection_return


@dataclasses.dataclass
class Style:
    title: str
    style: str

    def set_style(self, plate: "InspectionReturn"):
        plate.label_inspection_return.setText(self.title)
        plate.label_inspection_return.setStyleSheet(self.style)


class InspectionReturn(QWidget, Ui_inspection_return):
    def __init__(self, parent=None):
        super(InspectionReturn, self).__init__(parent)
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        self._timer = QTimer()
        self._timer.timeout.connect(self._reset)
        self.setVisible(False)

    def _reset(self):
        self.setVisible(False)
        style = Style(title="INSPECIONANDO....",
                      style="background-color: rgb(246, 211, 45);\ncolor: rgb(246, 245, 244);\nfont: 500 14pt \"Ubuntu\";")
        style.set_style(self)


    def approved(self):
        self.setVisible(True)
        style = Style(title="APROVADO",
                      style="background-color: rgb(3, 124, 27);\ncolor: rgb(246, 245, 244);\nfont: 500 14pt \"Ubuntu\";")
        style.set_style(self)
        self._timer.start(2500)


    def reproved(self):
        self.setVisible(True)
        style = Style(title="REPROVADO",
                      style="background-color: rgb(167, 24, 5);\ncolor: rgb(246, 245, 244);\nfont: 500 14pt \"Ubuntu\";")
        style.set_style(self)
        self._timer.start(2500)
