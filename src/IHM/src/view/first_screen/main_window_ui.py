# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 75))
        self.widget_2.setStyleSheet(u"background-color: #007A39;")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setFamilies([u"Helvetica Now Var Text Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: #00A336; color: white; border: 1px solid grey;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Helvetica Now Var Micro Medium"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: #007A39; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.button_model_c_2 = QPushButton(self.widget)
        self.button_model_c_2.setObjectName(u"button_model_c_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_model_c_2.sizePolicy().hasHeightForWidth())
        self.button_model_c_2.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Helvetica Now Var Micro Medium"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.button_model_c_2.setFont(font2)
        self.button_model_c_2.setStyleSheet(u"background-color: #008000; color: white;")

        self.gridLayout_4.addWidget(self.button_model_c_2, 1, 0, 1, 1)

        self.button_model_a_2 = QPushButton(self.widget)
        self.button_model_a_2.setObjectName(u"button_model_a_2")
        sizePolicy4.setHeightForWidth(self.button_model_a_2.sizePolicy().hasHeightForWidth())
        self.button_model_a_2.setSizePolicy(sizePolicy4)
        self.button_model_a_2.setFont(font2)
        self.button_model_a_2.setStyleSheet(u"background-color: #008000; color: white;")

        self.gridLayout_4.addWidget(self.button_model_a_2, 0, 0, 1, 1)

        self.button_model_d_2 = QPushButton(self.widget)
        self.button_model_d_2.setObjectName(u"button_model_d_2")
        sizePolicy4.setHeightForWidth(self.button_model_d_2.sizePolicy().hasHeightForWidth())
        self.button_model_d_2.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"Helvetica Now Var Text Medium"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.button_model_d_2.setFont(font3)
        self.button_model_d_2.setStyleSheet(u"background-color: #008000; color: white;")

        self.gridLayout_4.addWidget(self.button_model_d_2, 1, 1, 1, 1)

        self.button_model_b_2 = QPushButton(self.widget)
        self.button_model_b_2.setObjectName(u"button_model_b_2")
        sizePolicy4.setHeightForWidth(self.button_model_b_2.sizePolicy().hasHeightForWidth())
        self.button_model_b_2.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Ubuntu"])
        font4.setPointSize(15)
        font4.setBold(False)
        self.button_model_b_2.setFont(font4)
        self.button_model_b_2.setStyleSheet(u"background-color: #008000; color: white;")

        self.gridLayout_4.addWidget(self.button_model_b_2, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"INTELBRAS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESCOLHA O MODELO SWITCH PARA O TESTE", None))
        self.button_model_c_2.setText(QCoreApplication.translate("MainWindow", u"S 1108 F", None))
        self.button_model_a_2.setText(QCoreApplication.translate("MainWindow", u"SF 800 Q+", None))
        self.button_model_d_2.setText(QCoreApplication.translate("MainWindow", u"S 1108 G", None))
        self.button_model_b_2.setText(QCoreApplication.translate("MainWindow", u"SG 800 Q+", None))
    # retranslateUi

