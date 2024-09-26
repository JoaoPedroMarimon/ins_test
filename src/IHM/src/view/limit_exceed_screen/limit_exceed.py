from PySide6.QtWidgets import QDialog

from src.IHM.src.view.limit_exceed_screen.limit_exceed_screen_ui import Ui_Dialog

class LimitExceed(QDialog, Ui_Dialog):
    def __init__(self):
        super(LimitExceed, self).__init__()
        self.setupUi(self)