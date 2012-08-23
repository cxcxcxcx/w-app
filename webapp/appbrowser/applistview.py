# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMenu, QAction, QListView
from PyQt4.QtCore import QAbstractListModel

import os
import urllib2

from webapp.webapp import WebApp
from webapp import utils
from webapp.utils import getMyLogger

logger = getMyLogger("applistview")
kIconSize = 48

# For pyflakes
_ = __builtins__['_']


class AppListView(QListView):
    def __init__(self, *args):
        QListView.__init__(self, *args)
        self.setModel(
                AppListModel(
                    [WebApp.get_local_apps_dir(), utils.libFile('.')],
                    self))
        self.setIconSize(QtCore.QSize(kIconSize, kIconSize))

        self.downloadErrShown = False

    def contextMenuEvent(self, event):
        indexPos = self.indexAt(event.pos())
        actionCreate = QAction("Create new application...", self)
        actionCreateDesktop = QAction("Create desktop shortcut...", self)
        actionEdit = QAction("Edit...", self)
        actionClearLocal = QAction("Clear local data", self)
        actionRemoveApp = QAction("Remove App!", self)
        menu = QMenu()
        if indexPos.model() is None:
            # On blank area.
            menu.addAction(actionCreate)
        else:
            app = indexPos.model().getAppAtIndex(indexPos)
            print app.appInfo["name"]
            menu.addAction(actionCreateDesktop)
            menu.addAction(actionEdit)
            menu.addAction(actionClearLocal)
            menu.addAction(actionRemoveApp)

        act = menu.exec_(event.globalPos())
        if act is actionCreateDesktop:
            app.generateDesktop()
        elif act is actionEdit:
            app.edit()
        elif act is actionClearLocal:
            app.clear_local()
        elif act is actionCreate:
            self.parent().parent().createApp()
        elif act is actionRemoveApp:
            app.remove_app()
            self.model().loadData()
        #menu.popup(self.ui.listAppStock.mapToGlobal(pos))

    def showDownloadError(self):
        if self.downloadErrShown:
            return
        self.downloadErrShown = True
        QtGui.QMessageBox.warning(self, _("Download error"),
            _("Error occurred while downloading icons. ") +
            _("Please check internet connection."))


class AppListModel(QAbstractListModel):
    def __init__(self, root_path_l, parent=None):
        QAbstractListModel.__init__(self, parent=parent)
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
        if role == Qt.DisplayRole:
            return cur_app.appInfo["name"]
        elif role == Qt.DecorationRole:
            try:
                icon = QtGui.QPixmap()
                icon.loadFromData(
                        open(cur_app.get_app_icon(), 'rb').read())
                icon = icon.scaledToHeight(
                        kIconSize, Qt.SmoothTransformation)
                return icon
            except urllib2.URLError:
                # FIXME: Shouldn't reference a window here.
                QtCore.QTimer.singleShot(1, self.parentWin.showDownloadError)
                return QtCore.QVariant()
        elif role == Qt.SizeHintRole:
            return QtCore.QSize(140, 70)
        else:
            return QtCore.QVariant()

    def runApp(self, index):
        """Run the app at given index."""
        import subprocess
        import sys
        cur_app = self.getAppAtIndex(index)
        subprocess.Popen([sys.executable, sys.argv[0], cur_app.app_file])
