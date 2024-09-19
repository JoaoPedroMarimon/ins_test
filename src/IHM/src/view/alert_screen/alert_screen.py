from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QWidget, QDialog)

from src.IHM.src.view.alert_screen.alert_screen_ui import Ui_Dialog


class AlertScreen(QDialog, Ui_Dialog):
    def __init__(self):
        super(AlertScreen, self).__init__()
        self.setupUi(self)
        self.setVisible(False)
