#!/usr/bin/env python
# -*- coding=utf-8 -*-

from webapp.config import Config


class WebQQConfig(Config):
    defaultSetup = dict(Config.defaultSetup.items() + {
        'login_auto_run': True,
        'login_password': '',
        'login_status': '40',
        'hot_key': '<Alt>Q',
    }.items())

    def __init__(self, *args, **kargs):
        Config.__init__(self, *args, **kargs)

        self.login_states = ('10', '20', '30', '40', '50', '60', '70')
        self.login_states_dict = {
            '10': 0, '20': 1, '30': 2, '40': 3, '50': 4, '60': 5, '70': 6}

    def edit(self):
        from qqconfigwindow import ConfigWindow
        ConfigWindow(self.app, self)
