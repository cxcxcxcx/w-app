# -*- coding=utf-8 -*-
# The current version of this file partly comes from:
#   http://code.google.com/p/python-webqq/
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import re

QQ_DOWNLOAD_PATTERN = re.compile(
    'http://file[\d]+.web.qq.com/v[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/' +
    '[\d]+/[\d]+/[\d]+/[\d]+/f/'
)
QQ_LOGIN_PATTERN = re.compile('http://ui.ptlogin[\d]+.qq.com/cgi-bin/login')


def is_qq_download(uri):
    return QQ_DOWNLOAD_PATTERN.match(uri) != None


def is_qq_login(uri):
    return QQ_LOGIN_PATTERN.match(uri) != None
