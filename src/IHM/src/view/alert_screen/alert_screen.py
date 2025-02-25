from enum import Enum

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QWidget, QDialog)

from src.IHM.src.view.alert_screen.alert_screen_ui import Ui_Dialog

class AlertScreen(QDialog, Ui_Dialog):
    OnClose = Signal()
    def __init__(self):
        super(AlertScreen, self).__init__()
        self.setupUi(self)
        self.setVisible(False)
        self.button.clicked.connect(self.close)

    def closeEvent(self, event):
        self.OnClose.emit()
        event.accept()
    def open_screen(self,reason: str = 'camera'):
        match reason:
            case 'camera':
                self.titulo.setText("ERRO NA CÂMERA")
            case "arduino":
                self.titulo.setText("ERRO NO ARDUINO")
        self.setVisible(True)
