#!/usr/bin/env python3

from calibre.gui2.actions import InterfaceAction
from calibre_plugins.worddumb.main import ParseBook


class WordDumb(InterfaceAction):
    name = 'WordDumb'
    action_spec = ('WordDumb', None, 'Good morning Krusty Crew!', None)

    def genesis(self):
        icon = get_icons('starfish.svg')  # noqa: F821
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.run)

    def run(self):
        p = ParseBook(self.gui, self.plugin_path)
        p.parse()
