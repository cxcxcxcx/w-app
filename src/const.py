#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os

#URL = "http://web.qq.com/"
#URL = "https://mail.google.com/tasks/android"
#INIIAL_TITLE = "Q+ Web"
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
ICON = CURRENT_PATH + 'QQ.png'
VERSION = "1.4"
NAME = "pyWebQQ"
CONIFG_PATH = os.path.join(os.path.expanduser("~"), ".pywebqq/")
COOKIE_PATH = os.path.join(CONIFG_PATH, "cookie/")
COOKIE_FILE = COOKIE_PATH + "cookies.txt"
CONFIG_FILE = CONIFG_PATH + "WebQQ.conf"
