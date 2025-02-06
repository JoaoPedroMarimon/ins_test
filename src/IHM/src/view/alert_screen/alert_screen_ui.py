# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(490, 238)
        Dialog.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.titulo = QLabel(Dialog)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(40, 20, 391, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet(u"color: white")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 60, 291, 21))
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.button = QPushButton(Dialog)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(180, 150, 151, 31))
        font2 = QFont()
        font2.setBold(True)
        self.button.setFont(font2)
        self.button.setStyleSheet(u"background-color: rgb(248, 228, 92);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titulo.setText(QCoreApplication.translate("Dialog", u"ERRO NA CAM\u00caRA OU SERIAL", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Feche o programa e abra novamente", None))
        self.button.setText(QCoreApplication.translate("Dialog", u"Fechar", None))
    # retranslateUi

