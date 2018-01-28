#!/usr/bin/env python3
# coding: utf-8
## \file      nautilus-git-gui.py
## \author    SENOO, Ken
## \copyright CC0
## \date      created date: 2017-05-04T14:04+09:00
## \date      updated date: 2017-05-05T03:11+09:00

import os, subprocess, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject

class NautilusGitGUI(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def get_background_items(self, window, file):
        # Add the menu items
        items = []
        self.window = window
        items += [self._create_gitgui_item(file)]
        items += [self._create_gitk_item(file)]
        return items

    def _create_gitgui_item(self, file):
        item = Nautilus.MenuItem(name="NautilusGitGUI::GitGUI",
                                 label="Git GUI Here",
                                 tip="Git GUI Here")
        item.connect("activate", self._gitgui_run, file)
        return item

    def _create_gitk_item(self, file):
        item = Nautilus.MenuItem(name="NautilusGitGUI::GiTk",
                                 label="Gitk Here",
                                 tip="Gitk Here")
        item.connect("activate", self._gitk_run, file)
        return item

    def _gitgui_run(self, menu, file):
        subprocess.Popen(["git", "gui"], cwd=file.get_location().get_path())

    def _gitk_run(self, menu, file):
        subprocess.Popen(["gitk"], cwd=file.get_location().get_path())
