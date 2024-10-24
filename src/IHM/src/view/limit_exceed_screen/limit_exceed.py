from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from src.IHM.src.view.limit_exceed_screen.limit_exceed_screen_ui import Ui_Dialog

class LimitExceed(QDialog, Ui_Dialog):
    IsClicked = Signal()

    def __init__(self):
        super(LimitExceed, self).__init__()
        self.setupUi(self)
        self.button_continue.clicked.connect(self.on_continue_clicked)
        self.button_clicked = False

    def on_continue_clicked(self):
        self.IsClicked.emit()
        self.button_clicked = True
        self.setVisible(False)

    def has_user_clicked_continue(self):
        return self.button_clicked

    def open_limit_exceed_screen(self):
        self.setVisible(True)