# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'limit_exceed_screen.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(532, 630)
        Dialog.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, 9)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 700 22pt \"Ubuntu\";\n"
"color: rgb(246, 245, 244);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(9)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image = QLabel(self.widget)
        self.image.setObjectName(u"image")
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QSize(400, 400))
        self.image.setPixmap(QPixmap(u"perigo.png"))
        self.image.setScaledContents(True)
        self.image.setWordWrap(False)
        self.image.setMargin(60)
        self.image.setIndent(-1)
        self.image.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.image)


        self.verticalLayout.addWidget(self.widget)

        self.button_continue = QPushButton(Dialog)
        self.button_continue.setObjectName(u"button_continue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.button_continue.sizePolicy().hasHeightForWidth())
        self.button_continue.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.button_continue.setFont(font1)
        self.button_continue.setStyleSheet(u"background-color: #FFCC00; color: white;")

        self.verticalLayout.addWidget(self.button_continue)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"LIMITE DE PE\u00c7AS ULTRAPASSADO", None))
        self.image.setText("")
        self.button_continue.setText(QCoreApplication.translate("Dialog", u"CONTINUAR PROCESSO", None))
    # retranslateUi

