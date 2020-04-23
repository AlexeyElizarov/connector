# -*- coding: utf-8 -*-

"""
Implements interface to the WinShell.
"""


from subprocess import PIPE
from winshell import CommandPrompt, PowerShell

DRIVERS = {'commandprompt': CommandPrompt,
           'powershell': PowerShell}

STDOUT = {'pipe': PIPE,
          'none': None}


class Shell:

    def __init__(self, config):
        self._config = config
        self._interface = self._driver(stdout=self._stdout)

    @property
    def extension(self):
        return self._interface.extension

    @property
    def _driver(self):
        driver = self._config.get('driver', 'commandprompt').lower() or 'commandprompt'
        return DRIVERS[driver]

    @property
    def _stdout(self):
        stdout = self._config.get('stdout', 'pipe').lower() or 'pipe'
        return STDOUT[stdout]

    def execute(self, command):
        self._interface.open(command)

    def register(self, observer):
        self._interface.register(observer)
