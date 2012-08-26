# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appbrowse.ui'
#
# Created: Sun Aug 26 10:19:24 2012
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
        AppBrowser.resize(526, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("res/app_web.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppBrowser.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(AppBrowser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listAppStock = AppListView(self.centralwidget)
        self.listAppStock.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listAppStock.setResizeMode(QtGui.QListView.Adjust)
        self.listAppStock.setLayoutMode(QtGui.QListView.Batched)
        self.listAppStock.setSpacing(15)
        self.listAppStock.setViewMode(QtGui.QListView.IconMode)
        self.listAppStock.setUniformItemSizes(True)
        self.listAppStock.setBatchSize(1)
        self.listAppStock.setObjectName(_fromUtf8("listAppStock"))
        self.gridLayout.addWidget(self.listAppStock, 0, 0, 1, 2)
        AppBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AppBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        AppBrowser.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AppBrowser)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AppBrowser.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(AppBrowser)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        AppBrowser.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarApp = QtGui.QToolBar(AppBrowser)
        self.toolBarApp.setEnabled(False)
        self.toolBarApp.setObjectName(_fromUtf8("toolBarApp"))
        AppBrowser.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarApp)
        self.actionCreate = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.actionCreate.setIcon(icon)
        self.actionCreate.setObjectName(_fromUtf8("actionCreate"))
        self.actionRun = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("system-run"))
        self.actionRun.setIcon(icon)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionCreateDesktop = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("emblem-symbolic-link"))
        self.actionCreateDesktop.setIcon(icon)
        self.actionCreateDesktop.setObjectName(_fromUtf8("actionCreateDesktop"))
        self.actionEdit = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("accessories-text-editor"))
        self.actionEdit.setIcon(icon)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionClearLocal = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-clear"))
        self.actionClearLocal.setIcon(icon)
        self.actionClearLocal.setObjectName(_fromUtf8("actionClearLocal"))
        self.actionRemoveApp = QtGui.QAction(AppBrowser)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.actionRemoveApp.setIcon(icon)
        self.actionRemoveApp.setObjectName(_fromUtf8("actionRemoveApp"))
        self.toolBar.addAction(self.actionCreate)
        self.toolBarApp.addAction(self.actionRun)
        self.toolBarApp.addAction(self.actionCreateDesktop)
        self.toolBarApp.addAction(self.actionEdit)
        self.toolBarApp.addAction(self.actionClearLocal)
        self.toolBarApp.addAction(self.actionRemoveApp)

        self.retranslateUi(AppBrowser)
        QtCore.QObject.connect(self.listAppStock, QtCore.SIGNAL(_fromUtf8("activated(QModelIndex)")), AppBrowser.appActivated)
        QtCore.QObject.connect(self.toolBar, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.listAppStock.actionTriggered)
        QtCore.QObject.connect(self.toolBarApp, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.listAppStock.actionTriggered)
        QtCore.QMetaObject.connectSlotsByName(AppBrowser)

    def retranslateUi(self, AppBrowser):
        AppBrowser.setWindowTitle(QtGui.QApplication.translate("AppBrowser", "W-App!", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("AppBrowser", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarApp.setWindowTitle(QtGui.QApplication.translate("AppBrowser", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate.setText(QtGui.QApplication.translate("AppBrowser", "Create New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate.setToolTip(QtGui.QApplication.translate("AppBrowser", "Create new application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("AppBrowser", "Run!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setToolTip(QtGui.QApplication.translate("AppBrowser", "Run application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateDesktop.setText(QtGui.QApplication.translate("AppBrowser", "Create Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateDesktop.setToolTip(QtGui.QApplication.translate("AppBrowser", "Create desktop shortcut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setText(QtGui.QApplication.translate("AppBrowser", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setToolTip(QtGui.QApplication.translate("AppBrowser", "Edit application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearLocal.setText(QtGui.QApplication.translate("AppBrowser", "Clear local data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveApp.setText(QtGui.QApplication.translate("AppBrowser", "Remove App!", None, QtGui.QApplication.UnicodeUTF8))

from applistview import AppListView
