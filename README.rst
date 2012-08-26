==================================================
W-App: A real desktop application from Web pages
==================================================

**WARNING:
W-App IS IN ITS VERY EARLY STAGE AND STILL IN DEVELOPMENT, USE IT AT YOUR OWN
RISK!**

.. image:: http://chenxing.name/wapp_ss_thumb.png 
    :target: http://chenxing.name/wapp_screenshot.png
    :alt: Screenshot for W-App

W-App aims to turn a web application into a real desktop application. By
default, each application can have **a desktop entry** and **a system tray
icon**. For more application specific features, one can use W-App's **extension
interface** to create your own applications with system notification, automatic
log-in, and whatever you like. You will also be able to download applications
created by others.

You can easily create a local web application from a URL. Besides, some sample
applications are included in the package for your convenience:

* Google Calendar
* Google Mail
* Google Tasks
* 爱词霸 (An English-Chinese Dictionary)
* Web QQ (A popular IM in mainland China)
* Web Feixin (飞信, Another popular IM in China)

Among them, Web QQ has a customized interface (code mainly comes from another
open source project ``python-webqq``). Customization for other apps are still
in development.

I'm planning to start something like a "Web App Store" so that people can share
and download customized web applications.

Installation
~~~~~~~~~~~~
For **Archlinux** users, try it NOW by installing `w-app-git` from AUR.

For other distributions, please install Python 2 packages including
`pywebkitgtk`, `python-keybinder`, `python-notify`, `python-pyqt` and
`python-beautifulsoup3`. Names of these packages may vary. Python 3 will be
supported once the switch from PyGTK to PyQt is done.

For all **GNOME 3** users, we highly recommend the extension
https://github.com/rcmorano/gnome-shell-gnome2-notifications (AUR:
`gnome-shell-extension-gnome2-notifications-git`) to show tray icons in the top
panel. (Restarting GNOME Shell is required for the extension to be in effect)


What's Next?
~~~~~~~~~~~~~~~~
Short-period:

* Shortcuts to call out a application.
* Applications without tray.
* More comments for source codes.

Long-period:

* Prepare some APIs for creating desktop apps.
* Build an app store so that people can share and download wrappers from different web apps. 
* Rewrite the GTK+ codes in Qt and QWebkit.
* A tutorial for creating a new app with customizations.

If you'd like to suggest features, please do that by submitting an issue. Thanks! 

Fogger?
~~~~~~~
Unfortunately I started developing this app with my limited spare time before
Fogger was released. Nevertheless, after seeing Fogger, I believe this small
project is still meaningful because:

* It doesn't require Ubuntu or Unity.
* The design and idea are different in some areas. Extending an app with Python
  may not be too much harder than Javascript (as done in Fogger), but can make
  much more powerful features.

Acknowledgement
~~~~~~~~~~~~~~~
Currently lots of GTK+ and Webkit codes is copied with modification from
another open source project ``python-webqq``, which is available at:
http://code.google.com/p/python-webqq/

The current logo is from http://www.fasticon.com/ 
