# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionRecent_Files = QAction(MainWindow)
        self.actionRecent_Files.setObjectName(u"actionRecent_Files")
        self.actionchexiao = QAction(MainWindow)
        self.actionchexiao.setObjectName(u"actionchexiao")
        self.actionqianjian = QAction(MainWindow)
        self.actionqianjian.setObjectName(u"actionqianjian")
        self.actionguanyu = QAction(MainWindow)
        self.actionguanyu.setObjectName(u"actionguanyu")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionguanyu.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionRecent_Files)
        self.menu_2.addAction(self.actionchexiao)
        self.menu_2.addAction(self.actionqianjian)
        self.menu_3.addAction(self.actionguanyu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionRecent_Files.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u7684\u6587\u4ef6", None))
        self.actionchexiao.setText(QCoreApplication.translate("MainWindow", u"chexiao", None))
        self.actionqianjian.setText(QCoreApplication.translate("MainWindow", u"qianjian", None))
        self.actionguanyu.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

