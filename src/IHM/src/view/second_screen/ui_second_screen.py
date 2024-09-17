# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_screenXoIvcu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"background-color: #D9D9D9;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(190, 0, 611, 391))
        self.widget.setStyleSheet(u"background-color: white;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -30, 611, 421))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.approved_product = QLabel(self.widget)
        self.approved_product.setObjectName(u"approved_product")
        self.approved_product.setGeometry(QRect(0, 150, 611, 101))
        self.approved_product.setStyleSheet(u"background-color: #00A336; color: white;")
        self.approved_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rejected_product = QLabel(self.widget)
        self.rejected_product.setObjectName(u"rejected_product")
        self.rejected_product.setGeometry(QRect(0, 150, 611, 101))
        self.rejected_product.setStyleSheet(u"background-color: RED; color: white;")
        self.rejected_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.placard_team = QLabel(self.centralwidget)
        self.placard_team.setObjectName(u"placard_team")
        self.placard_team.setGeometry(QRect(0, 390, 801, 91))
        self.placard_team.setFont(font)
        self.placard_team.setStyleSheet(u"background-color: #008000; color: white;")
        self.placard_team.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 30, 191, 81))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: #008000; color: white;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 150, 171, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_product_one = QLabel(self.verticalLayoutWidget)
        self.label_product_one.setObjectName(u"label_product_one")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_product_one.setFont(font2)
        self.label_product_one.setStyleSheet(u"background-color: yellow;")
        self.label_product_one.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_product_one)

        self.label_product_two = QLabel(self.verticalLayoutWidget)
        self.label_product_two.setObjectName(u"label_product_two")
        self.label_product_two.setFont(font2)
        self.label_product_two.setStyleSheet(u"background-color: yellow;")
        self.label_product_two.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_product_two)

        self.label_product_three = QLabel(self.verticalLayoutWidget)
        self.label_product_three.setObjectName(u"label_product_three")
        self.label_product_three.setFont(font2)
        self.label_product_three.setStyleSheet(u"background-color: yellow;")
        self.label_product_three.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_product_three)

        self.placard_jiga = QLabel(self.centralwidget)
        self.placard_jiga.setObjectName(u"placard_jiga")
        self.placard_jiga.setEnabled(True)
        self.placard_jiga.setGeometry(QRect(0, 390, 811, 91))
        self.placard_jiga.setFont(font)
        self.placard_jiga.setStyleSheet(u"background-color: #6488ea")
        self.placard_jiga.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.switch_model = QLabel(self.centralwidget)
        self.switch_model.setObjectName(u"switch_model")
        self.switch_model.setGeometry(QRect(0, 360, 191, 31))
        self.switch_model.setStyleSheet(u"background-color: #00A336; color: white;")
        self.switch_model.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 110, 191, 21))
        self.label_2.setStyleSheet(u"background-color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_to_firstscreen = QPushButton(self.centralwidget)
        self.back_to_firstscreen.setObjectName(u"back_to_firstscreen")
        self.back_to_firstscreen.setGeometry(QRect(0, 0, 191, 31))
        self.back_to_firstscreen.setStyleSheet(u"background-color: RED; color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VIDEO", None))
        self.approved_product.setText(QCoreApplication.translate("MainWindow", u"APROVADO", None))
        self.rejected_product.setText(QCoreApplication.translate("MainWindow", u"REPROVADO", None))
        self.placard_team.setText(QCoreApplication.translate("MainWindow", u"EQUIPE AUTOMA\u00c7\u00c3O - INTELBRAS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HIST\u00d3RICO", None))
        self.label_product_one.setText(QCoreApplication.translate("MainWindow", u"INSPECIONANDO...", None))
        self.label_product_two.setText(QCoreApplication.translate("MainWindow", u"INSPECIONANDO...", None))
        self.label_product_three.setText(QCoreApplication.translate("MainWindow", u"INSPECIONANDO...", None))
        self.placard_jiga.setText(QCoreApplication.translate("MainWindow", u"INSPE\u00c7\u00c3O TAMPOGRAFIA SWITCH 8p", None))
        self.switch_model.setText(QCoreApplication.translate("MainWindow", u"MODELO SWITCH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00daLTIMAS TR\u00caS PE\u00c7AS", None))
        self.back_to_firstscreen.setText(QCoreApplication.translate("MainWindow", u"VOLTAR PARA MODELOS", None))
    # retranslateUi

