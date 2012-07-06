#!/usr/bin/env python
# -*- coding=utf-8 -*-

import gtk

from config import Config

from webapp.webapp import WebApp

class WebGTaskApp(WebApp):
    #URL = "https://mail.google.com/tasks/canvas"
    URL = "https://mail.google.com/tasks/android"
    INITIAL_TITLE = "Tasks"
    ICON = 'QQ.png'
    NAME = "Google Tasks App"
    CONF_PREFIX = "gtasks"

    SIZE = (470, 600)

class WebQQApp(WebApp):
    URL = "http://web.qq.com/"

    INITIAL_TITLE = "Q+ Web"
    ICON = 'QQ.png'
    NAME = "pyWebQQ"
    CONF_PREFIX = "gtasks"

    SIZE = (900, 600)

if __name__ == '__main__':
    config = Config()
    from webapp.webappview import WebAppView
    WebGTaskApp(WebAppView(config), config)
    #from webqqview import WebQQView
    #WebQQApp(WebQQView(config), config)
    gtk.main()
