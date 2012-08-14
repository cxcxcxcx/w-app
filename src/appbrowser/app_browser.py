# Copyright 2012 CHEN Xing (cx@chenxing.name)
# BSD 3-Clause license and disclaimer applies.

from PyQt4 import QtCore, QtGui
import os


def relPathToFullPath(relpath):
    app_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(app_path, '../', relpath)


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
        allApp = list(genAllApps())
        self.ui.listAppStock.setModel(AppListModel(allApp))
        self.ui.listAppStock.setIconSize(QtCore.QSize(48, 48))
        self.ui.statusbar.showMessage("Double click to start an app.")

        self.setWindowIcon(QtGui.QIcon(relPathToFullPath("res/app_web.png")))

    def appActivated(self, model_index):
        print model_index
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
        QtCore.QAbstractListModel.__init__(self, parent)
        self.app_list = app_list

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.app_list)

    def getAppAtIndex(self, index):
        return self.app_list[index.row()]

    def data(self, index, role):
        cur_app = self.getAppAtIndex(index)
        if role == QtCore.Qt.DisplayRole:
            return cur_app.appInfo["name"]
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(cur_app.get_app_icon())

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
