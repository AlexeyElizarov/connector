# -*- coding: utf-8 -*-

"""
Provides base interface to desktop based VPNs.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN
from abc import abstractmethod
from subprocess import Popen


class Desktop(VPN):
    """
    This is a base class for  desktop based VPN clients.
    This class provides methods to connect and disconnect to/from VPN using command line.
    """

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
        self._execute(self.connect_command)

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
