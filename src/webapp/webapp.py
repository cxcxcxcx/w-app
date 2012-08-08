#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk
import tray
import os

from mainwindow import MainWindow


class WebApp():
    def __init__(self, webviewCls, configCls):
        #config = Config()
        self.config = configCls(self)
        self.webview = webviewCls(self.config)
        self.window = MainWindow(self.webview, self)
        self.tray = tray.Tray(self)

    def get_app_icon(self, get_alt=False):
        """Get the path of application icon.

        Args:
            get_alt: Get alternative icon or not."""
        icon_name = self.appInfo["icon"]
        if get_alt:
            icon_name = self.appInfo.get("icon_alt", icon_name)
        icon_path = os.path.join(
            os.path.abspath(self.appDir),
            'res/%s' % icon_name)
        #if not os.path.exists(icon_path):
            #import urllib2
            #icon = urllib2.urlopen(self.appInfo["icon-url"])
            #with open(icon_path, "wb") as f:
                #f.write(icon.read())

        #print icon_path
        return icon_path

    def run(self):
        gtk.main()

    def get_user_dir(self):
        return os.path.expanduser(
                "~/.config/webapp/%s/" % self.appInfo["uuid"])

    def get_user_file(self, file_name, make_dir=False, touch_file=False):
        user_dir = self.get_user_dir()
        full_path = os.path.join(user_dir, file_name)
        if make_dir:
            full_dir = os.path.dirname(full_path)
            try:
                os.makedirs(full_dir, mode=0700)
            except OSError:
                pass

        if touch_file and not os.path.exists(full_path):
            print "CREATING"
            os.mknod(full_path)
        return full_path

    @classmethod
    def createWebApp(cls, url):
        import BeautifulSoup
        import urllib2
        soup = BeautifulSoup.BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers={'User-Agent': "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})))
        print soup
        print soup.title.string
        print soup.find("link", rel="shortcut icon")
        print soup.find("link")

