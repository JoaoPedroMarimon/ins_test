# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(247, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hist_one = QWidget(Form)
        self.hist_one.setObjectName(u"hist_one")
        self.hist_one.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.verticalLayout_6 = QVBoxLayout(self.hist_one)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.position = QLabel(self.hist_one)
        self.position.setObjectName(u"position")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.position.sizePolicy().hasHeightForWidth())
        self.position.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.position.setFont(font)
        self.position.setStyleSheet(u"")
        self.position.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.position.setIndent(-1)

        self.verticalLayout_6.addWidget(self.position)

        self.result = QLabel(self.hist_one)
        self.result.setObjectName(u"result")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy2)
        self.result.setStyleSheet(u"")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.result)


        self.verticalLayout.addWidget(self.hist_one)

        self.hist_two = QWidget(Form)
        self.hist_two.setObjectName(u"hist_two")
        self.hist_two.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.verticalLayout_7 = QVBoxLayout(self.hist_two)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.position_2 = QLabel(self.hist_two)
        self.position_2.setObjectName(u"position_2")
        sizePolicy1.setHeightForWidth(self.position_2.sizePolicy().hasHeightForWidth())
        self.position_2.setSizePolicy(sizePolicy1)
        self.position_2.setFont(font)
        self.position_2.setStyleSheet(u"")
        self.position_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.position_2.setIndent(-1)

        self.verticalLayout_7.addWidget(self.position_2)

        self.result_2 = QLabel(self.hist_two)
        self.result_2.setObjectName(u"result_2")
        sizePolicy2.setHeightForWidth(self.result_2.sizePolicy().hasHeightForWidth())
        self.result_2.setSizePolicy(sizePolicy2)
        self.result_2.setStyleSheet(u"")
        self.result_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.result_2)


        self.verticalLayout.addWidget(self.hist_two)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.position.setText("")
        self.result.setText(QCoreApplication.translate("Form", u"INSPECIONANDO....", None))
        self.position_2.setText("")
        self.result_2.setText(QCoreApplication.translate("Form", u"INSPECIONANDO....", None))
    # retranslateUi

