#!/usr/bin/env python2
# -*- coding=utf-8 -*-

import os
import sys
from webapp.webapp import WebApp


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


class AppFromFile(WebApp):
    def __init__(self, appFile, *args, **kargs):
        import json
        self.appInfo = json.load(open(appFile, "r"))
        self.appDir = os.path.dirname(appFile)

        sys.path.append(os.path.join(self.appDir, 'src'))

        from webapp.webappview import WebAppView
        from webapp.config import Config
        viewCls = loadClass(self.appInfo.get("view_class", None), WebAppView)
        confCls = loadClass(self.appInfo.get("conf_class", None), Config)

        WebApp.__init__(self, viewCls, confCls)

import gettext
gettext.install('messages', 'locale', unicode=True, names=['ngettext'])

if __name__ == '__main__':
    appFile = sys.argv[1]
    AppFromFile(appFile).run()
    #AppFromFile("apps/gtasks/gtasks.json").run()
    #AppFromFile("apps/webqq/webqq.json")
    #AppFromFile("apps/gcal/gcal.json").run()
    #gtk.main()
    #WebApp.createWebApp("https://www.google.com/calendar/render?tab=wc")
