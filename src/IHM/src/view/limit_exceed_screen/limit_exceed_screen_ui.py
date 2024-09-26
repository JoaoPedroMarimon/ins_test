# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'limit_exceed_screenEUJSDs.ui'
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
        Dialog.resize(360, 419)
        Dialog.setStyleSheet(u"background-color: #6488EA;")
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 320, 341, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_continue = QPushButton(self.horizontalLayoutWidget)
        self.button_continue.setObjectName(u"button_continue")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.button_continue.setFont(font)
        self.button_continue.setStyleSheet(u"background-color: #FFCC00; color: white;")

        self.horizontalLayout.addWidget(self.button_continue)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 170, 361, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.button_continue.setText(QCoreApplication.translate("Dialog", u"CONTINUAR PROCESSO", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"LIMITE DE PE\u00c7AS ULTRAPASSADO", None))
    # retranslateUi
