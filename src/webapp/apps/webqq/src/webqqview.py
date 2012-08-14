# -*- coding=utf-8 -*-
# The current version of this file partly comes from:
#   http://code.google.com/p/python-webqq/
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

import webbrowser
import qqutils
from webapp import utils
from webapp.webappview import WebAppView


class WebQQView(WebAppView):
    def __init__(self, app):
        self.hovered_uri = None
        WebAppView.__init__(self, app)

    def init_signals(self):
        WebAppView.init_signals(self)
        self.connect("create-web-view", self.create_webView)
        self.connect("hovering-over-link", self.hovering_over_ink)
        self.connect("navigation-policy-decision-requested", self.navigation_policy_decision_requested)
        self.connect("load-finished", self.load_finished)
        self.connect('title-changed', self.title_changed)

    def load_finished(self, view, frame):
        #print view.get_property('uri') + ':ok:' + frame.get_property('uri')
        frame_uri = frame.get_property('uri')
        if self.config["login_auto_run"] and self.config.app.appInfo["url"] == frame_uri:
            self.execute_script('alloy.portal.runApp(50);')
            return

        if qqutils.is_qq_login(frame_uri):
            self.execute_script("document.getElementById('ifram_login').contentWindow.document.getElementById('p').value='" + self.config["login_password"] + "';")
            self.execute_script("document.getElementById('ifram_login').contentWindow.onStateItemClick(" + self.config["login_status"] + ");")
            #if self.login_password != '':
            #    self.execute_script("document.getElementById('ifram_login').contentWindow.document.getElementById('loginform').submit();")

    def navigation_policy_decision_requested(self, view, frame, request, aciton, decision):
        if qqutils.is_qq_download(request.get_uri()):
            decision.download()
            return True
        return False

    def create_webView(self, view, frame):
        if self.hovered_uri:
            webbrowser.open_new_tab(self.hovered_uri)

    def hovering_over_ink(self, view, title, uri):
        self.hovered_uri = uri

    def title_changed(self, view, frame, title):
        windowtitle = self.app.window.get_title()
        if not title.startswith(self.app.appInfo["initial_title"]) and \
                not utils.same_title(windowtitle, title):
            self.app.notification(_("Notice"), title)
            self.app.tray.set_blinking(True)

        if title.startswith(self.app.appInfo["initial_title"]):
            self.app.tray.set_blinking(False)
        WebAppView.title_changed(self, view, frame, title)
