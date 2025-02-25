# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 242)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputBComboBox = QComboBox(Form)
        self.inputBComboBox.setObjectName(u"inputBComboBox")
        self.inputBComboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.inputBComboBox, 4, 1, 1, 1)

        self.inputAComboBox = QComboBox(Form)
        self.inputAComboBox.setObjectName(u"inputAComboBox")
        self.inputAComboBox.setMinimumSize(QSize(193, 40))
        self.inputAComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.inputAComboBox, 3, 1, 1, 1)

        self.orginDataLabel = QLabel(Form)
        self.orginDataLabel.setObjectName(u"orginDataLabel")
        self.orginDataLabel.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        self.orginDataLabel.setFont(font)
        self.orginDataLabel.setStyleSheet(u"color: rgb(120, 120, 120);")

        self.gridLayout.addWidget(self.orginDataLabel, 0, 0, 1, 1)

        self.inputBEditLine = QLineEdit(Form)
        self.inputBEditLine.setObjectName(u"inputBEditLine")
        self.inputBEditLine.setMinimumSize(QSize(0, 40))
        self.inputBEditLine.setReadOnly(True)

        self.gridLayout.addWidget(self.inputBEditLine, 4, 0, 1, 1)

        self.dataTypeComboBox = QComboBox(Form)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")

        self.gridLayout.addWidget(self.dataTypeComboBox, 2, 0, 1, 2)

        self.inputAEditLine = QLineEdit(Form)
        self.inputAEditLine.setObjectName(u"inputAEditLine")
        self.inputAEditLine.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.inputAEditLine, 3, 0, 1, 1)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(30)
        self.transDataLabel.setFont(font1)

        self.gridLayout.addWidget(self.transDataLabel, 1, 0, 1, 1)

        self.calcBtn = QPushButton(Form)
        self.calcBtn.setObjectName(u"calcBtn")
        self.calcBtn.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.calcBtn, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.orginDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.transDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.calcBtn.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

