# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspection_return.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_inspection_return(object):
    def setupUi(self, inspection_return):
        if not inspection_return.objectName():
            inspection_return.setObjectName(u"inspection_return")
        inspection_return.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inspection_return.sizePolicy().hasHeightForWidth())
        inspection_return.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(inspection_return)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_inspection_return = QLabel(inspection_return)
        self.label_inspection_return.setObjectName(u"label_inspection_return")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_inspection_return.sizePolicy().hasHeightForWidth())
        self.label_inspection_return.setSizePolicy(sizePolicy1)
        self.label_inspection_return.setMinimumSize(QSize(0, 90))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        font.setWeight(QFont.Medium)
        font.setItalic(False)
        self.label_inspection_return.setFont(font)
        self.label_inspection_return.setStyleSheet(u"background-color: rgb(246, 211, 45);\n"
"color: rgb(246, 245, 244);\n"
"font: 500 14pt \"Ubuntu\";")
        self.label_inspection_return.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_inspection_return)


        self.retranslateUi(inspection_return)

        QMetaObject.connectSlotsByName(inspection_return)
    # setupUi

    def retranslateUi(self, inspection_return):
        inspection_return.setWindowTitle(QCoreApplication.translate("inspection_return", u"Form", None))
        self.label_inspection_return.setText(QCoreApplication.translate("inspection_return", u"RETORNO DA INSPE\u00c7\u00c3O", None))
    # retranslateUi

