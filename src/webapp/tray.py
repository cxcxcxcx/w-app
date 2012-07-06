#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk, keybinder
import const, utils
from configwindow import ConfigWindow

class Tray():
    def __init__(self, app):
        self.window = app.window
        self.webview = app.webview
        self.config = app.config
        self.app = app
        self.blinking = False

        self.makePopup()

        self.isUnity = utils.is_unity()
        if self.isUnity:
            self.makeUnityTray()
        else:
            self.makeTray()
        self.webview.connect('title-changed', self.title_changed)
        keybinder.bind(self.config.hot_key, self.keybind_callback)

    def makeTray(self):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_file(self.app.ICON)
        self.tray.set_tooltip(self.app.NAME + ' ' + const.VERSION)
        self.tray.connect('activate', self.click_tray)
        self.tray.connect('popup-menu',
            lambda statusicon, button, activate_time: \
                self.pop_menu.popup(
                    None, None, None, 0, gtk.get_current_event_time()))

    def makeUnityTray(self):
        import appindicator
        self.tray = appindicator.Indicator(
                "example-simple-client",
                self.app.NAME,
                appindicator.CATEGORY_APPLICATION_STATUS)
        self.tray.set_status(appindicator.STATUS_ACTIVE)
        self.iconChange(self.app.ICON)
        self.tray.set_menu(self.pop_menu)

    def makePopup(self):
        pop_menu = gtk.Menu()
        item1 = gtk.MenuItem('显示/隐藏窗口')
        item1.connect("activate", self.click_tray)
        pop_menu.append(item1)

        item2 = gtk.MenuItem('配置...')
        item2.connect("activate", self.click_config)
        pop_menu.append(item2)

        item3 = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        item3.set_label('退出')
        item3.connect("activate", gtk.main_quit)
        pop_menu.append(item3)

        pop_menu.show_all()
        self.pop_menu = pop_menu
        #pop_menu.popup(None, None, None, 0, gtk.get_current_event_time())

    def iconChange(self, name):
        self.tray.set_icon(const.CURRENT_PATH + name)

    def title_changed(self, view, frame, title):
        windowtitle = self.window.get_title()
        if not title.startswith(self.app.INITIAL_TITLE) and not utils.same_title(windowtitle, title):
            utils.notification(self.app, "有新消息来了", title)
            if self.isUnity:
                self.iconChange('QQ1.png')
            else:
                self.tray.set_blinking(True)
            self.blinking = True
        if title.startswith(self.app.INITIAL_TITLE):
            if self.isUnity:
                self.iconChange('QQ.png')
            else:
                self.tray.set_blinking(False)
            self.blinking = False
        self.window.set_title(title)

    def keybind_callback(self):
        self.show_or_hide()

    def click_tray(self, widget):
        self.show_or_hide()

    def click_config(self, widget):
        ConfigWindow(self.webview, self, self.config)

    def show_or_hide(self):
        if self.window.is_active():
            self.window.hide()
        else:
            if self.blinking:
                self.iconChange('QQ.png')
                self.blinking = False
            self.window.present()
