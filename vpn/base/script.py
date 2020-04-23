# -*- coding: utf-8 -*-

"""
Implements VPN script interface.
Provides methods to execute script in a shell with VPN data fetched.
https://linuxhint.com/tempfile_python/
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from os import getcwd, remove
from os.path import join
from time import sleep
from helpers import SafeDict


class Script:
    def __init__(self, script, **kwargs):
        self._script = script
        self._driver = kwargs['driver']
        self._credentials = kwargs['credentials']
        self._shell = kwargs['shell']
        self._basename = 'temp' + self._shell.extension
        self._dirname = getcwd()
        self._path = join(self._dirname, self._basename)

    def execute(self):
        """
        Execute a script.
        :return:
        """

        try:
            # Prepare script string
            script = self._read()
            # Create temporary script file
            self._create(script)
            # Execute temporary script file
            self._execute()
        finally:
            # Remove temporary script file
            self._remove()

    def _create(self, script):
        """
        Create temporary script file out of script text.
        :return:
        """
        with open(self._path, 'w') as tmp:
            tmp.write(script)

    def _read(self) -> str:
        """
        Read script text file and fetch VPN data.
        :return: fetched shell script as string.
        """
        with open(self._script, 'r') as f:
            script = f.read()
            script = script.format_map(SafeDict(**vars(self._driver)))
            script = script.format_map(SafeDict(**vars(self._credentials)))
        return script

    def _remove(self):
        """
        Remove temporary script file.
        :return:
        """
        remove(self._path)

    def _execute(self):
        """
        Execute temporary script file with the shell.
        :return:
        """
        self._shell.execute(self._path)

