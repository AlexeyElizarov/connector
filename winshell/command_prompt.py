# -*- coding: utf-8 -*-

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from winshell import Shell
from subprocess import Popen


class CommandPrompt(Shell):
    """ Provides interface to Windows Command Prompt. """

    extension = '.cmd'

    def _open(self, command):
        return Popen(command, stdout=self._stdout)