# -*- coding: utf-8 -*-

"""
Implements parent class for VPN clients
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen
from abc import abstractmethod


class VPN:
    """
    This is a parent class for VPN clients.
    This class provides methods to connect and disconnect to/from VPN using command line.
    """

    _app = None  # Application ID

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

    def config(self, path):
        """
        Updates VPN attributes from configuration file/
        :param path: a path to a config file
        :return: None
        """

        config = self._read_config(path)
        for key, value in config.items():
            setattr(self, key, value)

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

    @staticmethod
    def _read_config(path: str = ''):
        """
        Reads configuration parameters from the file.
        :param file: a path to the connection config file.
        :return: config dictionary
        """
        config = dict()
        node = None

        with open(path, 'r') as f:
            config_file = f.readlines()

        for line in config_file:
            if line.startswith('['):
                node = line.strip()[1:-1]
                config[node] = dict()
            else:
                param, value = line.split('=')
                if node:
                    config[node][param.strip()] = value.strip()
                else:
                    config[param.strip()] = value.strip()

        return config