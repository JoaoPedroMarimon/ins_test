from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog
from src.IHM.src.view.limit_exceed_screen.limit_exceed_screen_ui import Ui_Dialog


class LimitExceed(QDialog, Ui_Dialog):
    IsClicked = Signal(bool)

    def __init__(self):
        super(LimitExceed, self).__init__()
        self.setupUi(self)
        warning_image = QPixmap("./src/static/perigo.png")

        self.image.setPixmap(warning_image)
        self.button_continue.clicked.connect(self.on_continue_clicked)

    def on_continue_clicked(self):
        self.IsClicked.emit(True)
        self.setVisible(False)



    def open_limit_exceed_screen(self):
        self.setVisible(True)