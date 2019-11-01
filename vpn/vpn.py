# -*- coding: utf-8 -*-

"""
Implements parent class for VPN clients
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen


class VPN:
    """
    This is a parent class for VPN clients.
    This class provides methods to connect and disconnect to/from VPN using command line.
    """
    
    def __init__(self, driver: str, config: str):
        """
        Initializes VPN client.
        :param driver: A path to a VPN client executable.
        :param config: A path to a configuration file that stores connection parameters.
        """
        self._driver = driver
        self._app = None 
        self._connect = str  # Command line to connect to VPN
        self._disconnect = str  # Command line to disconnect from VPN

        if config:
            with open(config) as _config:
                _attribs = _config.readlines()

            for attrib in _attribs:
                name, value = attrib.split('=')
                setattr(self, name.strip(), value.strip())

    def connect(self):
        """
        Connects to VPN using command line.
        :return: None
        """
        if self._connect:
            self._app = self._execute(self._connect)

    def disconnect(self):
        """
        Disconnects from VPN using command line.
        :return: 
        """
        if self._disconnect:
            self._execute(self._disconnect)

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