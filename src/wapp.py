#!/usr/bin/env python2
# -*- coding=utf-8 -*-

import sys
from webapp.webapp import WebApp

import gettext
gettext.install('messages', 'locale', unicode=True, names=['ngettext'])

if __name__ == '__main__':
    nargs = len(sys.argv)
    if nargs == 1:
        import gtk
        from app_browser import AppBrowser
        AppBrowser()
        gtk.main()
    else:
        appFile = sys.argv[1]
        app = WebApp(appFile)
        app.generateDesktop()
        app.run()
    #WebApp.createWebApp("https://www.google.com/calendar/render?tab=wc")
