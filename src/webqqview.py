#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os, webkit, ctypes, webbrowser
import const, utils

try:
	libwebkit = ctypes.CDLL('libwebkitgtk-1.0.so.0')
except:
	try:
		libwebkit = ctypes.CDLL('libwebkit-1.0.so.2')
	except:
		libwebkit = ctypes.CDLL('libwebkitgtk-1.0.so')

libgobject = ctypes.CDLL('libgobject-2.0.so.0')
libsoup = ctypes.CDLL('libsoup-2.4.so.1')

from webapp.webappview import WebAppView

class WebGTaskView(WebAppView):
    def __init__(self, config):
        WebAppView.__init__(self, config)

WebQQView = WebGTaskView

class WebQQView_(WebAppView):
#class WebQQView(WebAppView):
	def __init__(self, config):
		WebAppView.__init__(self, config)
		self.hovered_uri = None
		self.config = config
		self.init_signals()

	def init_signals(self):
		self.connect('mime-type-policy-decision-requested', self.policy_decision_requested)
		self.connect('download-requested', self.download_requested)
		self.connect("create-web-view", self.create_webView)
		self.connect("hovering-over-link", self.hovering_over_ink)
		self.connect("navigation-policy-decision-requested", self.navigation_policy_decision_requested)
		self.connect("load-finished", self.load_finished)

	def load_finished(self, view, frame):
		#print view.get_property('uri') + ':ok:' + frame.get_property('uri')
		frame_uri = frame.get_property('uri')
		if self.config.login_auto_run == 'yes' and const.URL == frame_uri:
			self.execute_script('alloy.portal.runApp(50);')
			return

		if utils.is_qq_login(frame_uri):
			self.execute_script("document.getElementById('ifram_login').contentWindow.document.getElementById('p').value='" + self.config.login_password + "';")
			self.execute_script("document.getElementById('ifram_login').contentWindow.onStateItemClick(" + self.config.login_status + ");")
			#if self.login_password != '':
			#	self.execute_script("document.getElementById('ifram_login').contentWindow.document.getElementById('loginform').submit();")

	def navigation_policy_decision_requested(self, view, frame, request, aciton, decision):
		if utils.is_qq_download(request.get_uri()):
			decision.download()
			return True
		return False

	def policy_decision_requested(self, view, frame, request, mimetype, decision):
		if self.can_show_mime_type(mimetype):
			return False
		decision.download()
		return True

	def download_requested(self, view, download):
		download.connect('notify::status', self.download_status)
		download.set_destination_uri('file://' + self.config.save_path + '/' + download.get_suggested_filename())
		return True

	def download_status(self, download, pspec):
		if download.get_status() == -1:
			utils.notification("文件下载失败", self.config.save_path + '/' + download.get_suggested_filename())
		if download.get_status() == 1:
			utils.notification("文件开始下载", self.config.save_path + '/' + download.get_suggested_filename())
		if download.get_status() == 3:
			utils.notification("文件下载完成", self.config.save_path + '/' + download.get_suggested_filename())

	def create_webView(self, view, frame):
		if self.hovered_uri:
			webbrowser.open_new_tab(self.hovered_uri)

	def hovering_over_ink(self, view, title, uri):
		self.hovered_uri = uri
