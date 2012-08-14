# -*- coding: utf-8 -*-
# Copyright 2012 CHEN Xing (cx@chenxing.name)
# Licensed under the terms of the BSD 3-Clause.

from distutils.core import setup
import os
import os.path as osp


def get_data(dname, exclude=[]):
    """Return data files in dname with prefix"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dname):
        for fname in filenames:
            if not fname.startswith('.') and \
                    not osp.splitext(fname)[1] in exclude:
                file_str = osp.join(dirpath, fname)
                flist.append(file_str[file_str.index('/') + 1:])
    return flist

setup(name="W-App",
      version="0.0.1",
      description='Web page as local application!',
      long_description="""
Change any web page into an app with a tray icon. Extension friendly.""",
      author="CHEN Xing",
      license='New BSD',
      platforms=['any'],
      packages=['webapp'],
      package_data={
          'webapp': get_data('webapp/apps/', exclude=['.pyc']) + \
                    get_data('webapp/res') + get_data('webapp/locale'),
                    },
      scripts=['wapp']
)
