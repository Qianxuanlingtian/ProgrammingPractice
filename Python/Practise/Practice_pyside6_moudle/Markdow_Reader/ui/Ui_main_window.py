# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextBrowser, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOptions = QAction(MainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.centralWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 1, 2, 1)

        self.listWidget = QListWidget(self.centralWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTool = QMenu(self.menubar)
        self.menuTool.setObjectName(u"menuTool")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addAction(self.actionExit)
        self.menuTool.addAction(self.actionSearch)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u9605\u8bfb\u5668", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e", None))
#if QT_CONFIG(shortcut)
        self.actionSearch.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9009\u9879", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menuTool.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

