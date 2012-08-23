# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

from PyQt4 import QtCore, QtGui
import os
import urllib2
from webapp import utils
from webapp.webapp import WebApp

from webapp.utils import getMyLogger
logger = getMyLogger("webapp")

kIconSize = 48


def genAllApps():
    app_path = utils.libFile('.')
    for root, dirs, files in os.walk(app_path):
        for i_file in files:
            if i_file.endswith(".json"):
                yield WebApp(os.path.join(root, i_file))

    for root, dirs, files in os.walk(WebApp.get_local_apps_dir()):
        for i_file in files:
            if i_file.endswith("app.json"):
                try:
                    app = WebApp(os.path.join(root, i_file))
                    yield app
                except Exception as e:
                    logger.error("%s" % e)


class AppBrowser(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        from ui_appbrowse import Ui_AppBrowser
        self.ui = Ui_AppBrowser()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(
            utils.libFile(utils.WAPP_ICON)))

        QtCore.QTimer.singleShot(1, self.loadApps)

    def loadApps(self):
        """Load applications and icons"""
        self.ui.statusbar.showMessage(
            _("Loading apps and preparing icons... "
                "(can be slow for the first time)"))
        QtCore.QCoreApplication.processEvents()

        self.downloadErrShown = False

        self.ui.listAppStock.setModel(
                AppListModel(
                    [WebApp.get_local_apps_dir(), utils.libFile('.')],
                    self))
        self.ui.listAppStock.setIconSize(QtCore.QSize(kIconSize, kIconSize))
        self.ui.statusbar.showMessage("Double click to start an app.")

    def showDownloadError(self):
        if self.downloadErrShown:
            return
        self.downloadErrShown = True
        QtGui.QMessageBox.warning(self, _("Download error"),
            _("Error occurred while downloading icons. ") +
            _("Please check internet connection."))

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
        print self.ui.listAppStock.model()
        self.ui.listAppStock.model().loadData()

    @classmethod
    def run(cls):
        import sys
        app = QtGui.QApplication(sys.argv)
        obj = cls()
        obj.show()
        sys.exit(app.exec_())


class AppListModel(QtCore.QAbstractListModel):
    def __init__(self, root_path_l, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent=parent)
        self.parentWin = parent
        self.root_path_l = root_path_l
        self.loadData()

    def loadData(self):
        self.app_list = list(self.genAllApps())
        self.app_list.sort(key=lambda x: x.appInfo["name"])
        self.emit(QtCore.SIGNAL("dataChanged"))

    def genAllApps(self):
        """Load all applications in the specific path."""
        for root_path in self.root_path_l:
            for root, dirs, files in os.walk(root_path):
                for i_file in files:
                    if i_file.endswith("app.json"):
                        try:
                            app = WebApp(os.path.join(root, i_file))
                            yield app
                        except Exception as e:
                            logger.error("%s" % e)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.app_list)

    def getAppAtIndex(self, index):
        return self.app_list[index.row()]

    def data(self, index, role):
        cur_app = self.getAppAtIndex(index)
        if role == QtCore.Qt.DisplayRole:
            return cur_app.appInfo["name"]
        elif role == QtCore.Qt.DecorationRole:
            try:
                icon = QtGui.QPixmap(cur_app.get_app_icon())
                icon = icon.scaledToHeight(
                        kIconSize, QtCore.Qt.SmoothTransformation)
                return icon
            except urllib2.URLError:
                # FIXME: Shouldn't reference a window here.
                QtCore.QTimer.singleShot(1, self.parentWin.showDownloadError)
                return QtCore.QVariant()
        elif role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(140, 70)
        else:
            return QtCore.QVariant()

    def runApp(self, index):
        """Run the app at given index."""
        import sys
        import subprocess
        cur_app = self.getAppAtIndex(index)
        subprocess.Popen([sys.executable, sys.argv[0], cur_app.app_file])

if __name__ == '__main__':
    import gettext
    gettext.install('messages', 'locale', unicode=True, names=['ngettext'])
    AppBrowser.run()
