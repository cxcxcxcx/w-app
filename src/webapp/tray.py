# -*- coding=utf-8 -*-
# The current version of this file partly comes from:
#   http://code.google.com/p/python-webqq/
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# BSD 3-Clause license and disclaimer applies.

import gtk
import keybinder
import utils


class Tray():
    def __init__(self, app):
        self.window = app.window
        self.webview = app.webview
        self.config = app.config
        self.app = app
        self.blinking = False

        self.icon = self.app.get_app_icon()
        self.icon_alt = self.app.get_app_icon(get_alt=True)

        self.makePopup()

        self.isUnity = utils.is_unity()
        if self.isUnity:
            self.makeUnityTray()
        else:
            self.makeTray()
        if self.config["hot_key"]:
            keybinder.bind(self.config["hot_key"], self.keybind_callback)

    def makeTray(self):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_file(self.icon)
        self.tray.set_tooltip(self.app.appInfo["name"])
        self.tray.connect('activate', self.click_tray)
        self.tray.connect('popup-menu',
            lambda statusicon, button, activate_time: \
                self.pop_menu.popup(
                    None, None, None, 0, gtk.get_current_event_time()))

    def makeUnityTray(self):
        import appindicator
        self.tray = appindicator.Indicator(
                "example-simple-client",
                self.app.appInfo["name"],
                appindicator.CATEGORY_APPLICATION_STATUS)
        self.tray.set_status(appindicator.STATUS_ACTIVE)
        self.change_icon(self.icon)
        self.tray.set_menu(self.pop_menu)

    def makePopup(self):
        pop_menu = gtk.Menu()
        item1 = gtk.MenuItem(_('Show/Hide Window'))
        item1.connect("activate", self.click_tray)
        pop_menu.append(item1)

        item2 = gtk.MenuItem(_('Configure...'))
        item2.connect("activate", self.click_config)
        pop_menu.append(item2)

        item3 = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        item3.set_label(_('Exit'))
        item3.connect("activate", gtk.main_quit)
        pop_menu.append(item3)

        pop_menu.show_all()
        self.pop_menu = pop_menu
        #pop_menu.popup(None, None, None, 0, gtk.get_current_event_time())

    def change_icon(self, name):
        if self.isUnity:
            self.tray.set_icon(name)
        else:
            self.tray.set_from_file(self.icon)

    def set_blinking(self, blink):
        self.blinking = blink
        if self.isUnity:
            self.change_icon(
                self.icon_alt if blink else self.icon)
        else:
            self.tray.set_blinking(blink)

    def keybind_callback(self):
        self.show_or_hide()

    def click_tray(self, widget):
        self.show_or_hide()

    def click_config(self, widget):
        self.config.edit()

    def show_or_hide(self):
        if self.window.is_active():
            self.window.hide()
        else:
            if self.blinking:
                self.set_blinking(False)
            self.window.present()
