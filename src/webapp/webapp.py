#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk
import tray
import os
#import BeautifulSoup

from mainwindow import MainWindow


class WebApp():
    def __init__(self, webviewCls, configCls):
        #config = Config()
        self.config = configCls(self)
        self.webview = webviewCls(self.config)
        self.window = MainWindow(self.webview, self)
        self.tray = tray.Tray(self)

    def get_app_icon(self):
        return os.path.join(
            os.path.abspath(self.appDir),
            'res/%s' % self.appInfo["icon"])

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
    #@classmethod
    #def createWebApp(cls, url):
        #import urllib2
        #webpage = urllib2.urlopen(url).read()

        #import re
        #re.compile(r'link')
        #appIcon
