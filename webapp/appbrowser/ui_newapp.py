# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newapp.ui'
#
# Created: Wed Aug 22 21:28:21 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewApp(object):
    def setupUi(self, NewApp):
        NewApp.setObjectName(_fromUtf8("NewApp"))
        NewApp.resize(349, 149)
        self.verticalLayout = QtGui.QVBoxLayout(NewApp)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(NewApp)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.editURL = QtGui.QLineEdit(self.groupBox)
        self.editURL.setObjectName(_fromUtf8("editURL"))
        self.gridLayout.addWidget(self.editURL, 1, 1, 1, 2)
        self.editAppName = QtGui.QLineEdit(self.groupBox)
        self.editAppName.setObjectName(_fromUtf8("editAppName"))
        self.gridLayout.addWidget(self.editAppName, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(NewApp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewApp)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewApp.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewApp.reject)
        QtCore.QMetaObject.connectSlotsByName(NewApp)
        NewApp.setTabOrder(self.editAppName, self.editURL)
        NewApp.setTabOrder(self.editURL, self.buttonBox)

    def retranslateUi(self, NewApp):
        NewApp.setWindowTitle(QtGui.QApplication.translate("NewApp", "Create Application", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NewApp", "Create New App", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewApp", "Full URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewApp", "WebApp Name:", None, QtGui.QApplication.UnicodeUTF8))

