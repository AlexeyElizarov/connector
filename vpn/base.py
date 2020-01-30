# -*- coding: utf-8 -*-

"""
Implements parent class for VPN clients
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen
from abc import abstractmethod
from configparser import ConfigParser


class VPN:
    """
    This is a parent class for VPN clients.
    This class provides methods to connect and disconnect to/from VPN using command line.
    """

    _app = None  # Application ID
    _config = None  # A path to configuration file

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        config = ConfigParser()
        config.read(value)

        for key, value in config['DEFAULT'].items():
            print(key, value)
            setattr(self, key, value)

    @property
    @abstractmethod
    def connect_command(self):
        """Must be implemented with concrete connect command"""
        pass

    @property
    @abstractmethod
    def disconnect_command(self):
        """Must be implemented with concrete disconnect command"""
        pass

    def connect(self):
        """
        Connects to VPN using command line.
        :return: None
        """

        self._app = self._execute(self.connect_command)

    def disconnect(self):
        """
        Disconnects from VPN using command line.
        :return: None
        """
        self._execute(self.disconnect_command)

    @staticmethod
    def _execute(commands):
        """
        Private method to execute commands in command line.
        :param commands: commands to execute. May be a string or a list. 
        :return: None
        """
        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            Popen(command, shell=True)