#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pynotify, os

def notification(app, content, title):
	pynotify.init(app.INITIAL_TITLE)
	notify = pynotify.Notification(content, title, app.ICON)
	notify.set_urgency(pynotify.URGENCY_NORMAL)
	notify.set_timeout(3)
	notify.show()

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
