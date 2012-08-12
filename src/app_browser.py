import gtk
import os


def relPathToFullPath(relpath):
    app_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(app_path, relpath)


def getAllApps():
    from webapp.webapp import WebApp
    app_path = relPathToFullPath('.')
    for root, dirs, files in os.walk(app_path):
        for i_file in files:
            if i_file.endswith(".json"):
                yield WebApp(os.path.join(root, i_file))


class AppBrowser(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.set_default_size(800, 600)
        self.set_title("W-App!")
        self.set_wmclass("W-App!", "W-App!")
        self.set_icon_from_file(relPathToFullPath("res/app_web.png"))

        liststore = gtk.ListStore(gtk.gdk.Pixbuf, str)
        appview = gtk.IconView(liststore)
        appview.set_pixbuf_column(0)
        appview.set_text_column(1)

        for i_app in getAllApps():
            pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(
                    i_app.get_app_icon(), 64, 64)
            liststore.append([pixbuf, i_app.appInfo["name"]])

        self.connect("destroy", lambda w: gtk.main_quit())
        self.add(appview)
        self.show_all()

if __name__ == '__main__':
    import gettext
    gettext.install('messages', 'locale', unicode=True, names=['ngettext'])
    AppBrowser()
    gtk.main()
