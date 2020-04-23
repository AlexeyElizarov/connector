# -*- coding: utf-8 -*-

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from winshell import Shell
from subprocess import Popen


class PowerShell(Shell):
    """ Provides interface to PowerShell. """

    extension = '.ps1'

    def _open(self, command):
        return Popen(['powershell', command], stdout=self._stdout)

