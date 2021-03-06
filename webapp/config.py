#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import json
import utils


class Config(object):
    # Redefine the "defaultSetup" in a subclass
    defaultSetup = {
        'proxy_enable': False,
        'proxy_uri': 'http://127.0.0.1:8000',
        'hot_key': None,
        'save_path': utils.get_user_download_dir()
    }

    def __init__(self, app):
        self.app = app
        self.conf_file = self.app.get_user_file("conf.json", make_dir=True)

        try:
            self.conf = json.load(open(self.conf_file, "r"))
        except IOError:
            print "FILE NOT FOUND"
            self.conf = self.defaultSetup
            self.save()

    def __getitem__(self, y):
        try:
            return self.conf[y]
        except KeyError:
            self.conf[y] = self.defaultSetup[y]
            return self.conf[y]

    def __setitem__(self, y, new):
        self.conf[y] = new

    def save(self):
        with open(self.conf_file, 'w') as f:
            json.dump(self.conf, f, ensure_ascii=False, indent=4)

    def reload(self):
        print "reload config..."

    def edit(self):
        utils.openEditor(self.conf_file)
