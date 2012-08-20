# -*- coding=utf-8 -*-
# The current version of this file partly comes from:
#   http://code.google.com/p/python-webqq/
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import gtk


class MainWindow(gtk.Window):
    def __init__(self, webview, app):
        self.app = app
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_icon_from_file(app.get_app_icon())

        self.set_default_size(*app.appInfo["size"])
        self.set_size_request(10, 10)

        self.set_title(app.appInfo["name"])
        self.set_wmclass(app.appInfo["name"], app.appInfo["name"])
        self.webview = webview
        self.add(self.webview)
        self.webview.open(app.appInfo["url"])
        self.connect("delete_event", self.minimize)

        self.set_position(gtk.WIN_POS_CENTER)
        self.show_all()

    def minimize(self, widget, event, data=None):
        self.hide()
        return True
