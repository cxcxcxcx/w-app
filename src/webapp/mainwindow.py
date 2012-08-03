#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk

class MainWindow(gtk.Window):
    def __init__(self, webview, app):
        self.app = app
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_icon_from_file(app.get_app_icon())
        #self.set_default_size(900, 600)
        self.set_default_size(*app.appInfo["size"])
        self.set_title(app.appInfo["initial_title"])
        self.webview = webview
        self.add(self.webview)
        self.webview.open(app.appInfo["url"])
        self.connect("delete_event", self.minimize)
        self.connect('check-resize', self.check_resize)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show_all()

    def check_resize(self, window):
        self.set_size_request(*self.app.appInfo["size"])
        #self.set_size_request(900, 600)

    def minimize(self, widget, event, data = None):
        self.hide()
        return True
