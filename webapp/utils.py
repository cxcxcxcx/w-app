# -*- coding=utf-8 -*-
# The current version of this file partly comes from:
#   http://code.google.com/p/python-webqq/
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import os
import logging

import gettext
lib_path = os.path.dirname(os.path.realpath(__file__))

_ = gettext.translation('messages',
        os.path.join(lib_path, 'locale'),
        fallback=True
    ).ugettext
gettext.install('messages',
    os.path.join(lib_path, 'locale'),
    unicode=True, names=['ngettext'])

WAPP_ICON = "res/wapp.png"


def libFile(relpath):
    return os.path.join(lib_path, relpath)


def openEditor(file_path):
    """Open a file editor"""
    import subprocess
    subprocess.call(['xdg-open', file_path])


def getMyLogger(name, level=logging.INFO):
    """Get a logger with a name"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.handlers:
        return logger
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(levelname)s:%(name)s-- %(message)s"))
    logger.addHandler(handler)
    return logger


def ensure_dir_exists(path, mode=0o700):
    try:
        os.makedirs(path, mode=mode)
        #logger.info("Dir %s created" % full_dir)
    except OSError:
        pass


def is_unity():
    desktop_env = os.getenv('DESKTOP_SESSION')
    if desktop_env != None:
        return desktop_env.startswith('ubuntu')
    return False


def same_title(t1, t2):
    t1 = t1.decode("utf-8").replace(" ", "")
    t2 = t2.decode("utf-8").replace(" ", "")
    l = len(t1)
    if l != len(t2):
        return False
    for i in range(l):
        if t1 == shift_string(t2, i):
            return True
    return False


def shift_string(string, i):
    return string[i:] + string[:i]


def read_config(ini_path):
    """May throw exception if error occurs."""
    print ini_path
    import StringIO
    import ConfigParser
    ini_str = '[root]\n' + open(ini_path, 'r').read()
    ini_fp = StringIO.StringIO(ini_str)
    config = ConfigParser.RawConfigParser()
    config.readfp(ini_fp)
    return config


def get_user_download_dir():
    try:
        user_dir_file = read_config(
                os.path.expanduser("~/.config/user-dirs.dirs"))
        download_dir_val = user_dir_file.get('root', 'XDG_DOWNLOAD_DIR')
        prefix = download_dir_val.strip('"').split("/")[0]
        if prefix:
            download_dir = os.path.expanduser("~/") + \
                        "/".join(download_dir_val.strip('"').split("/")[1:])
            print download_dir
            return download_dir
        return download_dir_val.strip('"')
    except:
        # TODO: Log it
        return os.path.expanduser("~/")
