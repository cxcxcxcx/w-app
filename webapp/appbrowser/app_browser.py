# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

from PyQt4 import QtCore, QtGui
import os
from webapp import utils


def relPathToFullPath(relpath):
    return os.path.join(
            utils.lib_path, relpath)


def genAllApps():
    from webapp.webapp import WebApp
    app_path = relPathToFullPath('.')
    for root, dirs, files in os.walk(app_path):
        for i_file in files:
            if i_file.endswith(".json"):
                yield WebApp(os.path.join(root, i_file))


class AppBrowser(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        from ui_appbrowse import Ui_AppBrowser
        self.ui = Ui_AppBrowser()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(relPathToFullPath("res/wapp.png")))

        QtCore.QTimer.singleShot(1, self.loadApps)

    def loadApps(self):
        """Load applications and icons"""
        self.ui.statusbar.showMessage(
            _("Loading apps and preparing icons... "
                "(can be slow for the first time)"))
        QtCore.QCoreApplication.processEvents()

        self.downloadErrShown = False

        allApp = list(genAllApps())

        self.ui.listAppStock.setModel(AppListModel(allApp, self))
        self.ui.listAppStock.setIconSize(QtCore.QSize(48, 48))
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
        app_list = self.ui.listAppStock
        app = app_list.model().getAppAtIndex(
                app_list.currentIndex())
        app.generateDesktop()

    @classmethod
    def run(cls):
        import sys
        app = QtGui.QApplication(sys.argv)
        obj = cls()
        obj.show()
        sys.exit(app.exec_())


class AppListModel(QtCore.QAbstractListModel):
    def __init__(self, app_list, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent=parent)
        self.parentWin = parent
        self.app_list = app_list
        self.app_list.sort(key=lambda x: x.appInfo["name"])

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.app_list)

    def getAppAtIndex(self, index):
        return self.app_list[index.row()]

    def data(self, index, role):
        cur_app = self.getAppAtIndex(index)
        if role == QtCore.Qt.DisplayRole:
            return cur_app.appInfo["name"]
        elif role == QtCore.Qt.DecorationRole:
            import urllib2
            try:
                return QtGui.QIcon(cur_app.get_app_icon())
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