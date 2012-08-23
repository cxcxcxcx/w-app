# -*- coding=utf-8 -*-
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import json
import gtk
import shutil
import sys
import os
import urllib2
import uuid

from mainwindow import MainWindow

import tray
import utils
from utils import getMyLogger
logger = getMyLogger("webapp")


def loadClass(confList, default):
    if confList is None:
        return default

    try:
        modName, clsName = confList
        return getattr(__import__(modName), clsName)
    except:
        logger.error("Cannot load specified module or class")
        raise


class WebApp():
    def __init__(self, app_file):
        self.appInfo = json.load(open(app_file, "r"))
        self.app_file = os.path.abspath(app_file)
        self.app_dir = os.path.dirname(app_file)

    def edit(self):
        utils.openEditor(self.app_file)

    def get_desktop_path(self):
        return os.path.expanduser(
                "~/.local/share/applications/wapp-%s.desktop" %
                    self.appInfo["uuid"])

    def generateDesktop(self):
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
                'name': "%s (W-App)" % self.appInfo["name"],
                'exec': os.path.abspath(sys.argv[0]),
                'app_file': self.app_file,
                'icon': self.get_app_icon()
                }
        desktopPath = self.get_desktop_path()
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

        # If the icon doesn't exist, download to a local dir.
        local_path = self.get_user_file(icon_name)
        if os.path.exists(local_path):
            return local_path

        if not "icon-url" in self.appInfo:
            logger.debug("No icon available..")
            return utils.libFile(utils.WAPP_ICON)
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

    def clear_local(self):
        """Clear local caches and cookies..."""
        shutil.rmtree(self.get_conf_dir(self.appInfo["uuid"]))

    def remove_app(self):
        """Remove the app!"""
        try:
            os.remove(self.get_desktop_path())
        except OSError as e:
            if e.errno == 2:
                # File not found.
                pass
            else:
                raise e
        shutil.rmtree(self.app_dir)

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
        return self.get_conf_dir(self.appInfo["uuid"])

    def get_user_file(self, file_name, make_dir=True, touch_file=False):
        user_dir = self.get_user_dir()
        full_path = os.path.join(user_dir, file_name)
        if make_dir:
            full_dir = os.path.dirname(full_path)
            utils.ensure_dir_exists(full_dir)

        if touch_file and not os.path.exists(full_path):
            logger.info("Creating file %s" % full_path)
            os.mknod(full_path)
        return full_path

    @classmethod
    def get_conf_dir(cls, subdir=""):
        return os.path.expanduser(
                "~/.config/webapp/%s/" % subdir)

    @classmethod
    def get_local_apps_dir(cls, subdir=""):
        return cls.get_conf_dir("apps/%s/" % subdir)

    @classmethod
    def createWebApp(cls, name, url):
        """Create a new application by name and url."""
        if len(name.strip()) == 0:
            raise ValueError("Name is empty!")

        import BeautifulSoup
        soup = BeautifulSoup.BeautifulSoup(
                urllib2.urlopen(
                    urllib2.Request(
                        url,
                        headers={'User-Agent':
                            "Mozilla/5.0 (X11; U; Linux i686) " +
                            "Gecko/20071127 Firefox/2.0.0.11"
                        })))
        appJson = {
            'uuid': str(uuid.uuid4()),
            'name': name,
            'url': url,
            'icon': 'icon.png',
            'size': [800, 600],
        }
        icon_url = soup.find("link", rel="apple-touch-icon")
        if icon_url is None:
            icon_url = soup.find("link", rel="shortcut icon")
            appJson['icon'] = 'icon.ico'
        if icon_url:
            appJson['icon-url'] = icon_url['href']

        app_dir = cls.get_local_apps_dir(appJson['uuid'])
        utils.ensure_dir_exists(app_dir)
        with open("%s/%s" % (app_dir, 'app.json'), 'w') as f:
            json.dump(appJson, f, ensure_ascii=False, indent=4)
