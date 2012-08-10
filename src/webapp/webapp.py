#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk
import tray
import os
import sys

from mainwindow import MainWindow


def loadClass(confList, default):
    if confList is None:
        return default

    try:
        modName, clsName = confList
        return getattr(__import__(modName), clsName)
    except:
        raise
        print "Use default class"
        return default


class WebApp():
    def __init__(self, app_file):
        import json
        self.appInfo = json.load(open(app_file, "r"))
        self.app_file = os.path.abspath(app_file)
        self.app_dir = os.path.dirname(app_file)

    def generateDesktop(self):
        print sys.argv[0]
        template = \
"""[Desktop Entry]
Encoding=UTF-8
Name=%(name)s
Type=Application
Exec=%(exec)s %(app_file)s
Icon=%(icon)s
Terminal=false
GenericName=MyApp
"""
        desktopStr = template % {
                'name': self.appInfo["name"],
                'exec': os.path.abspath(sys.argv[0]),
                'app_file': self.app_file,
                'icon': self.get_app_icon()
                }
        desktopPath = os.path.expanduser(
                "~/.local/share/applications/wapp-%s.desktop" %
                    self.appInfo["name"])
        # TODO: Catch exception
        # TODO: Ensure the directory exists
        with open(desktopPath, "w") as f:
            f.write(desktopStr)

    def get_app_icon(self, get_alt=False):
        """Get the path of application icon.

        Args:
            get_alt: Get alternative icon or not."""
        icon_name = self.appInfo["icon"]
        if get_alt:
            icon_name = self.appInfo.get("icon_alt", icon_name)
        icon_path = os.path.join(
            os.path.abspath(self.app_dir),
            'res/%s' % icon_name)

        if os.path.exists(icon_path):
            return icon_path
        else:
            # If the icon doesn't exist, download to a local dir.
            local_path = self.get_user_file(icon_name)
            if os.path.exists(local_path):
                return local_path

            import urllib2
            icon = urllib2.urlopen(self.appInfo["icon-url"]).read()
            with open(local_path, "wb") as f:
                f.write(icon)
            return local_path

    def notification(self, content, title):
        """Show a notification"""
        import pynotify
        pynotify.init(self.appInfo["initial_title"])
        notify = pynotify.Notification(content, title, self.get_app_icon())
        notify.set_urgency(pynotify.URGENCY_NORMAL)
        notify.set_timeout(3)
        notify.show()

    def run(self):
        sys.path.append(os.path.join(self.app_dir, 'src'))

        from webappview import WebAppView
        from config import Config
        view_cls = loadClass(self.appInfo.get("view_class", None), WebAppView)
        conf_cls = loadClass(self.appInfo.get("conf_class", None), Config)

        self.config = conf_cls(self)
        self.webview = view_cls(self)
        self.window = MainWindow(self.webview, self)
        self.tray = tray.Tray(self)
        gtk.main()

    def get_user_dir(self):
        return os.path.expanduser(
                "~/.config/webapp/%s/" % self.appInfo["uuid"])

    def get_user_file(self, file_name, make_dir=True, touch_file=False):
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
        soup = BeautifulSoup.BeautifulSoup(
                urllib2.urlopen(
                    urllib2.Request(
                        url,
                        headers={'User-Agent':
                            "Mozilla/5.0 (X11; U; Linux i686) " +
                            "Gecko/20071127 Firefox/2.0.0.11"
                        })))
        print soup
        print soup.title.string
        print soup.find("link", rel="shortcut icon")
        print soup.find("link")
