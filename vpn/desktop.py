# -*- coding: utf-8 -*-

"""
Provides base interface to desktop based VPNs.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN
from abc import abstractmethod
from subprocess import Popen, PIPE


class Desktop(VPN):
    """
    This is a base class for  desktop based VPN clients.
    This class provides methods to connect and disconnect to/from VPN using command line.
    """

    output = str  # Output from command execution.
    is_connected = False  # VPN connection status.

    class Decorators:
        """
        This class provides Desktop VPN private decorators
        """

        @staticmethod
        def status_change(func):
            """
            Calls _update_status method after execution of func.
            """
            def wrapped(*args):
                self = args[0]
                func(self)
                self._update_status()
            return wrapped

    @abstractmethod
    def _update_status(self):
        """Abstract method to update IS_CONNECTED attribute."""
        pass

    @property
    @abstractmethod
    def _connect_command(self):
        """Must be implemented with concrete connect command"""
        pass

    @property
    @abstractmethod
    def _disconnect_command(self):
        """Must be implemented with concrete disconnect command"""
        pass

    @Decorators.status_change
    def connect(self):
        """
        Connects to VPN using command line.
        :return: None
        """
        self._execute(self._connect_command)

    @Decorators.status_change
    def disconnect(self):
        """
        Disconnects from VPN using command line.
        :return: None
        """
        self._execute(self._disconnect_command)

    def _execute(self, commands):
        """
        Executes commands in command line.
        :param commands: commands to execute. May be a string or a list.
        :return: None
        """
        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            process = Popen(command, stdout=PIPE)
            self.output = str(process.stdout.read())
