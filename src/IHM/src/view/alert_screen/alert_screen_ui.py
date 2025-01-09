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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(360, 420)
        Dialog.setStyleSheet(u"background-color: #6488EA;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 290, 361, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 301, 271))
        self.label.setPixmap(QPixmap(u"projetos/inspecao-tampografia-switch-8p/docs_image/alert_background.png"))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 320, 361, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_restart = QPushButton(self.horizontalLayoutWidget)
        self.button_restart.setObjectName(u"button_restart")
        self.button_restart.setStyleSheet(u"background-color: #00A336; color: white;")

        self.horizontalLayout.addWidget(self.button_restart)

        self.button_turn_off = QPushButton(self.horizontalLayoutWidget)
        self.button_turn_off.setObjectName(u"button_turn_off")
        self.button_turn_off.setStyleSheet(u"background-color: red; color: white;")

        self.horizontalLayout.addWidget(self.button_turn_off)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ERRO NA CAM\u00caRA OU SERIAL", None))
        self.label.setText("")
        self.button_restart.setText(QCoreApplication.translate("Dialog", u"REINICIAR", None))
        self.button_turn_off.setText(QCoreApplication.translate("Dialog", u"DESLIGAR", None))
    # retranslateUi

