# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

from PyQt4 import QtCore, QtGui
import sys
import urllib2
from webapp import utils
from webapp.webapp import WebApp

# For pyflakes
_ = __builtins__['_']

from webapp.utils import getMyLogger
logger = getMyLogger("webapp")


class AppBrowser(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        from ui_appbrowse import Ui_AppBrowser
        self.ui = Ui_AppBrowser()
        self.ui.setupUi(self)
        self.ui.listAppStock.win = self
        self.setWindowIcon(QtGui.QIcon(
            utils.libFile(utils.WAPP_ICON)))

        QtCore.QTimer.singleShot(1, self.loadApps)
        QtCore.QCoreApplication.setAttribute(
                QtCore.Qt.AA_DontShowIconsInMenus, False)

    def loadApps(self):
        """Load applications and icons"""
        self.ui.statusbar.showMessage(
            _("Loading apps and preparing icons... "
                "(can be slow for the first time)"))
        QtCore.QCoreApplication.processEvents()

        self.ui.statusbar.showMessage("Double click to start an app.")

    def appActivated(self, model_index):
        model_index.model().runApp(model_index)

    def genDesktopEntry(self):
        """Generate desktop entry for current selected app."""
        app_list = self.ui.listAppStock
        app = app_list.model().getAppAtIndex(
                app_list.currentIndex())
        app.generateDesktop()

    def createApp(self):
        """Create a new application from a URL."""
        dialog = QtGui.QDialog()
        from ui_newapp import Ui_NewApp
        dialog.ui = Ui_NewApp()
        dialog.ui.setupUi(dialog)

        while True:
            if not dialog.exec_():
                # Cancelled.
                return
            try:
                WebApp.createWebApp(
                    str(dialog.ui.editAppName.text()),
                    str(dialog.ui.editURL.text()))
                break
            except ValueError as e:
                QtGui.QMessageBox.warning(self, _("Error"),
                    _("Error %s") % e.message)
            except urllib2.URLError as e:
                QtGui.QMessageBox.warning(self, _("Error"),
                    _("Network Error %s") % e.message)
        self.ui.listAppStock.model().loadData()

    @classmethod
    def run(cls):
        app = QtGui.QApplication(sys.argv)
        obj = cls()
        obj.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    import gettext
    gettext.install('messages', 'locale', unicode=True, names=['ngettext'])
    AppBrowser.run()
