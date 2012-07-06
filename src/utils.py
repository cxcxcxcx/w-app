#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re, os
from inifile import IniFile

QQ_DOWNLOAD_PATTERN = re.compile('http://file[\d]+.web.qq.com/v[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/[\d]+/f/')
QQ_LOGIN_PATTERN = re.compile('http://ui.ptlogin[\d]+.qq.com/cgi-bin/login')

def is_qq_download(uri):
	return QQ_DOWNLOAD_PATTERN.match(uri) != None

def is_qq_login(uri):
	return QQ_LOGIN_PATTERN.match(uri) != None

def get_user_download_dir():
	user_dir_file = IniFile(os.path.join(os.path.expanduser("~"), ".config/user-dirs.dirs"))
	download_dir_val = user_dir_file.get_value('XDG_DOWNLOAD_DIR')
	prefix = download_dir_val.strip('"').split("/")[0]
	if prefix:
		return os.getenv("HOME") + "/" + "/".join(download_dir_val.strip('"').split("/")[1:])
	return download_dir_val.strip('"')
