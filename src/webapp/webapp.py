#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk
import tray

from mainwindow import MainWindow

class WebApp():
    def __init__(self, webview, config):
        #config = Config()
        self.config = config
        self.webview = webview
        self.window = MainWindow(self.webview, self)
        self.tray = tray.Tray(self)

    def run(self):
        gtk.main()
