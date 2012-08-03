#!/usr/bin/env python2
# -*- coding=utf-8 -*-

import gtk

import os
import sys
from webapp.config import Config
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
        #print json.dumps(dict(conf.items("app")), indent=4)
        import json
        self.appInfo = json.load(open(appFile, "r"))
        self.appDir = os.path.dirname(appFile)
        print self.appInfo

        sys.path.append(os.path.join(self.appDir, 'src'))

        from webapp.webappview import WebAppView
        viewCls = loadClass(self.appInfo.get("view_class", None), WebAppView)
        confCls = loadClass(self.appInfo.get("conf_class", None), Config)

        WebApp.__init__(self, viewCls, confCls)

if __name__ == '__main__':
    #AppFromFile("apps/gtasks/gtasks.json")
    AppFromFile("apps/webqq/webqq.json")
    #AppFromFile("apps/gtasks.json", WebAppView, Config)
    #WebGTaskApp(WebAppView(config), config)
    #from webqqview import WebQQView
    #WebQQApp(WebQQView(config), config)
    gtk.main()
