# -*- coding: utf-8 -*-

"""
Provides base API to remote desktop software, e.g. MS RDP and Teamviewer.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen
from configparser import ConfigParser
from abc import abstractmethod


class RDC:
    """
    This is a base class for remote desktop software.
    """

    _config = None
    _app = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        config = ConfigParser()
        config.read(value)

        for key, value in config['DEFAULT'].items():
            setattr(self, key, value)

    @property
    @abstractmethod
    def open_command(self):
        """Must be implemented with concrete open command"""
        pass

    @property
    @abstractmethod
    def close_command(self):
        """Must be implemented with concrete close command"""
        pass

    def open(self):
        """
        Opens remote desktop using command line.
        :return: None
        """
        self._execute(self.open_command)

    def close(self):
        """
        Closses remote desktop using command line.
        :return: None
        """
        self._execute(self.close_command)

    def _execute(self, commands):
        """
        Private method to execute commands in command line.
        :param commands: commands to execute. May be a string or a list.
        :return: None
        """
        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            self._app = Popen(command, shell=True)
