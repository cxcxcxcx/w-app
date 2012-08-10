#!/usr/bin/env python
# -*- coding=utf-8 -*-

import webkit
import ctypes

try:
    libwebkit = ctypes.CDLL('libwebkitgtk-1.0.so.0')
except:
    try:
        libwebkit = ctypes.CDLL('libwebkit-1.0.so.2')
    except:
        libwebkit = ctypes.CDLL('libwebkitgtk-1.0.so')

libgobject = ctypes.CDLL('libgobject-2.0.so.0')
libsoup = ctypes.CDLL('libsoup-2.4.so.1')


class WebAppView(webkit.WebView):
    def __init__(self, app):
        webkit.WebView.__init__(self)
        #self.hovered_uri = None
        self.config = app.config
        self.app = app
        self.init_settings()
        self.init_cookie()
        self.init_proxy()
        self.init_signals()

    def init_settings(self):
        settings = self.get_settings()
        #settings.set_property("auto-resize-window", False)
        settings.set_property('enable-universal-access-from-file-uris', True)
        settings.set_property('enable-file-access-from-file-uris', True)
        settings.set_property('enable-page-cache', True)
        settings.set_property('enable-spatial-navigation', True)
        settings.set_property('enable-site-specific-quirks', True)
        #settings.set_property('user-agent', 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
        self.set_settings(settings)
        #settings.set_property('user-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.4+ (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.4+')

    def init_cookie(self):
        cookie_file = self.config.app.get_user_file(
            "cookies.txt", make_dir=True, touch_file=True)
        cookie_file = str(cookie_file)
        session = libwebkit.webkit_get_default_session()
        soup_cookie = libsoup.soup_cookie_jar_text_new(cookie_file, False)
        if soup_cookie < 0:
            raise Exception("Incorrect cookie value: %s" % (soup_cookie))
        libsoup.soup_session_add_feature(session, soup_cookie)

    def init_proxy(self):
        if self.config["proxy_enable"]:
            session = libwebkit.webkit_get_default_session()
            libgobject.g_object_set(
                session, 'proxy-uri', self.config["proxy_uri"], None)

    def init_signals(self):
        self.connect(
                'mime-type-policy-decision-requested',
                self.policy_decision_requested)
        self.connect('download-requested', self.download_requested)
        self.connect('title-changed', self.title_changed)

    def download_requested(self, view, download):
        download.connect('notify::status', self.download_status)
        download.set_destination_uri(
                'file://' + self.config["save_path"] + '/' +
                    download.get_suggested_filename())
        return True

    def download_status(self, download, pspec):
        file_name = self.config["save_path"] + '/' + \
                        download.get_suggested_filename()
        if download.get_status() == -1:
            self.app.notification(_("Download Failed"), file_name)
        if download.get_status() == 1:
            self.app.notification(_("File download started"), file_name)
        if download.get_status() == 3:
            self.app.notification(_("File download completed"), file_name)

    def policy_decision_requested(self, view, frame, request, mimetype, decision):
        if self.can_show_mime_type(mimetype):
            return False
        decision.download()
        return True

    def title_changed(self, view, frame, title):
        self.app.window.set_title(title)

    #def load_finished(self, view, frame):
        ##print view.get_property('uri') + ':ok:' + frame.get_property('uri')
        #frame_uri = frame.get_property('uri')
        #if self.config.login_auto_run == 'yes' and const.URL == frame_uri:
            #self.execute_script('alloy.portal.runApp(50);')
            #return

    #def navigation_policy_decision_requested(self, view, frame, request, aciton, decision):
        #if utils.is_qq_download(request.get_uri()):
            #decision.download()
            #return True
        #return False

    #def create_webView(self, view, frame):
        #if self.hovered_uri:
            #webbrowser.open_new_tab(self.hovered_uri)

    #def hovering_over_ink(self, view, title, uri):
        #self.hovered_uri = uri
