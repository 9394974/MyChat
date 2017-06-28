from decorator import lazy_property
from components import Finder

import itchat


class MyChat(object):

    def __init__(self):
        self.commands = {
            'Dir': Finder()
        }
        itchat.msg_register([itchat.content.TEXT])(self.parse_command)

    def init(self, debug=True):
        itchat.auto_login(hotReload=debug)
        itchat.run()

    def parse_command(self, msg):
        args = msg['Content'].split()
        if args[0] in self.commands:
            component = self.commands[args[0]]
            return component.parse_commands(msg, args[1:])

