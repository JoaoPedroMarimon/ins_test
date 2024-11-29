# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(952, 591)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_to_model_screen = QPushButton(self.widget_3)
        self.button_to_model_screen.setObjectName(u"button_to_model_screen")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_to_model_screen.sizePolicy().hasHeightForWidth())
        self.button_to_model_screen.setSizePolicy(sizePolicy2)
        self.button_to_model_screen.setStyleSheet(u"background-color: rgb(224, 27, 36);\n"
"color: rgb(246, 245, 244);")

        self.verticalLayout_2.addWidget(self.button_to_model_screen)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"font: 500 13pt \"Ubuntu\";\n"
"background-color: rgb(13, 116, 18);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(10)
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.widget_5.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_hist_one = QLabel(self.widget_4)
        self.label_hist_one.setObjectName(u"label_hist_one")
        self.label_hist_one.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.label_hist_one.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_hist_one)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_hist_two = QLabel(self.widget_6)
        self.label_hist_two.setObjectName(u"label_hist_two")
        self.label_hist_two.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.label_hist_two.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_hist_two)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.model_label = QLabel(self.widget_3)
        self.model_label.setObjectName(u"model_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.model_label.sizePolicy().hasHeightForWidth())
        self.model_label.setSizePolicy(sizePolicy5)
        self.model_label.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(246, 245, 244);")
        self.model_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.model_label)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.video_place = QWidget(self.widget)
        self.video_place.setObjectName(u"video_place")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.video_place.sizePolicy().hasHeightForWidth())
        self.video_place.setSizePolicy(sizePolicy6)
        self.video_place.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.horizontalLayout_3 = QHBoxLayout(self.video_place)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.video_place)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_placard = QLabel(self.widget_2)
        self.label_placard.setObjectName(u"label_placard")
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_placard.setFont(font)
        self.label_placard.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 132, 228);")
        self.label_placard.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_placard)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_to_model_screen.setText(QCoreApplication.translate("Form", u"VOLTAR PARA MODELOS", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"HIST\u00d3RICO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u00daLTIMAS DUAS PE\u00c7AS", None))
        self.label_hist_one.setText(QCoreApplication.translate("Form", u"INSPECIONANDO....", None))
        self.label_hist_two.setText(QCoreApplication.translate("Form", u"INSPECIONANDO....", None))
        self.model_label.setText(QCoreApplication.translate("Form", u"MODEL SWITCH", None))
        self.label_placard.setText(QCoreApplication.translate("Form", u"EQUIPE AUTOMA\u00c7\u00c3O - INTELBRAS", None))
    # retranslateUi

