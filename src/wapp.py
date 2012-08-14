#!/usr/bin/env python2
# -*- coding=utf-8 -*-
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# BSD 3-Clause license and disclaimer applies.

import sys
from webapp.webapp import WebApp

import gettext
import os

app_path = os.path.dirname(os.path.realpath(__file__))
gettext.install('messages',
    os.path.join(app_path, 'locale'),
    unicode=True, names=['ngettext'])

if __name__ == '__main__':
    nargs = len(sys.argv)
    if nargs == 1:
        from appbrowser.app_browser import AppBrowser
        AppBrowser.run()
    else:
        appFile = sys.argv[1]
        app = WebApp(appFile)
        app.run()
