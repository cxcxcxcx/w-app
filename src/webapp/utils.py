#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os


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
    print ini_path
    import StringIO
    import ConfigParser
    try:
        ini_str = '[root]\n' + open(ini_path, 'r').read()
        ini_fp = StringIO.StringIO(ini_str)
        config = ConfigParser.RawConfigParser()
        config.readfp(ini_fp)
        return config
    except:
        return None


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
        # TODO: what to return?
        raise
