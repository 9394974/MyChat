from components.Base import BaseComponent

from decorator import specific_people
from config import START_DIR

import os
import os.path
import itchat


class Finder(BaseComponent):

    TO_USER = 'filehelper'

    def __init__(self, start_dir=START_DIR):
        self.commands = {
            'init': self.init,
            'cd': self.cd,
            'ls': self.ls,
            'file': self.file
        }
        self.start_dir = start_dir
        self.current_dir = start_dir
        os.chdir(self.current_dir)

    def init(self, msg, extra):
        """

        :param msg:
        :param extra:
        :return:
         返回初始目录下的文件信息
        """
        if not os.path.exists(self.start_dir):
            itchat.send('Dir init失败，初始目录不存在', toUserName=Finder.TO_USER)
            return

        not_hidden = list(filter(lambda name: not name.startswith('.'), os.listdir(self.start_dir)))
        dir_repr = ''
        file_repr = ''
        for name in not_hidden:
            new_name = os.path.join(self.start_dir, name)
            if os.path.isdir(new_name):
                dir_repr += '目录：{}\n'.format(name)
            elif os.path.isfile(new_name):
                file_repr += '文件: {}\n'.format(name)

        itchat.send(dir_repr + file_repr, toUserName=Finder.TO_USER)

    def cd(self, msg, extra):
        dir_name = extra[0]
        new_path = os.path.join(self.current_dir, dir_name)
        if not os.path.isdir(new_path):
            itchat.send('Dir cd失败, 该路径非目录', toUserName=Finder.TO_USER)
            return

        os.chdir(new_path)
        self.current_dir = os.getcwd()
        itchat.send("Dir cd成功, 当前目录为{}".format(self.current_dir), toUserName=Finder.TO_USER)

    def ls(self, msg, extra):
        if not os.path.exists(self.current_dir):
            itchat.send('Dir ls失败，当前目录{}不存在'.format(self.current_dir), toUserName=Finder.TO_USER)
            return

        not_hidden = list(filter(lambda name: not name.startswith('.'), os.listdir(self.current_dir)))
        dir_repr = ''
        file_repr = ''
        for name in not_hidden:
            new_name = os.path.join(self.current_dir, name)
            if os.path.isdir(new_name):
                dir_repr += '目录：{}\n'.format(name)
            elif os.path.isfile(new_name):
                file_repr += '文件: {}\n'.format(name)

        itchat.send(dir_repr + file_repr, toUserName=Finder.TO_USER)

    def file(self, msg, extra):
        file_name = extra[0]
        new_path = os.path.join(self.current_dir, file_name)
        if not os.path.isfile(new_path):
            itchat.send("Dir file失败, {}并非文件".format(new_path), toUserName=Finder.TO_USER)
            return

        if not itchat.send_file(new_path, toUserName=Finder.TO_USER):
            itchat.send("Dir file失败")

    @specific_people(name=TO_USER)
    def parse_commands(self, msg, extra, *args, **kwargs):
        command = 'error' if not extra else extra[0]
        if command in self.commands:
            self.commands[command](msg, extra[1:])
        else:
            itchat.send("Dir 子命令错误", toUserName=Finder.TO_USER)



