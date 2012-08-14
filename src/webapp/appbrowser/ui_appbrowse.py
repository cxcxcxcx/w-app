# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appbrowse.ui'
#
# Created: Tue Aug 14 13:15:45 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AppBrowser(object):
    def setupUi(self, AppBrowser):
        AppBrowser.setObjectName("AppBrowser")
        AppBrowser.resize(495, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/app_web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppBrowser.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(AppBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(92, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(92, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.listAppStock = QtGui.QListView(self.centralwidget)
        self.listAppStock.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listAppStock.setSpacing(5)
        self.listAppStock.setViewMode(QtGui.QListView.IconMode)
        self.listAppStock.setUniformItemSizes(True)
        self.listAppStock.setObjectName("listAppStock")
        self.gridLayout.addWidget(self.listAppStock, 1, 0, 1, 4)
        AppBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AppBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        AppBrowser.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AppBrowser)
        self.statusbar.setObjectName("statusbar")
        AppBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(AppBrowser)
        QtCore.QObject.connect(self.listAppStock, QtCore.SIGNAL("activated(QModelIndex)"), AppBrowser.appActivated)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), AppBrowser.genDesktopEntry)
        QtCore.QMetaObject.connectSlotsByName(AppBrowser)

    def retranslateUi(self, AppBrowser):
        AppBrowser.setWindowTitle(QtGui.QApplication.translate("AppBrowser", "W-App!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AppBrowser", "Generate desktop entry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("AppBrowser", "Create", None, QtGui.QApplication.UnicodeUTF8))

