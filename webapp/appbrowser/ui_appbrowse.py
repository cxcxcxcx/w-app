# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appbrowse.ui'
#
# Created: Wed Aug 22 18:41:43 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AppBrowser(object):
    def setupUi(self, AppBrowser):
        AppBrowser.setObjectName(_fromUtf8("AppBrowser"))
        AppBrowser.resize(495, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("res/app_web.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppBrowser.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(AppBrowser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(92, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(92, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.listAppStock = QtGui.QListView(self.centralwidget)
        self.listAppStock.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listAppStock.setResizeMode(QtGui.QListView.Adjust)
        self.listAppStock.setLayoutMode(QtGui.QListView.Batched)
        self.listAppStock.setSpacing(15)
        self.listAppStock.setViewMode(QtGui.QListView.IconMode)
        self.listAppStock.setUniformItemSizes(True)
        self.listAppStock.setBatchSize(1)
        self.listAppStock.setObjectName(_fromUtf8("listAppStock"))
        self.gridLayout.addWidget(self.listAppStock, 1, 0, 1, 4)
        AppBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AppBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        AppBrowser.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AppBrowser)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AppBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(AppBrowser)
        QtCore.QObject.connect(self.listAppStock, QtCore.SIGNAL(_fromUtf8("activated(QModelIndex)")), AppBrowser.appActivated)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AppBrowser.genDesktopEntry)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), AppBrowser.createApp)
        QtCore.QMetaObject.connectSlotsByName(AppBrowser)

    def retranslateUi(self, AppBrowser):
        AppBrowser.setWindowTitle(QtGui.QApplication.translate("AppBrowser", "W-App!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AppBrowser", "Generate desktop entry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("AppBrowser", "Create", None, QtGui.QApplication.UnicodeUTF8))

