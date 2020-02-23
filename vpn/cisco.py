# -*- coding: utf-8 -*-

"""
Provides interface to Cisco VPN Client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import Desktop


class Cisco(Desktop):
    """
    Provides interface to Cisco VPN Client.
    """

    _driver = r'C:\Program Files (x86)\Cisco Systems\VPN Client\vpnclient.exe'
    _config = 'cisco.ini'

    @property
    def _connect_command(self):
        return f'"{self._driver}" connect {getattr(self, "profile")} '\
            f'user {getattr(self, "user")} ' \
            f'pwd {getattr(self, "pwd")}'

    @property
    def _disconnect_command(self):
        return f'"{self._driver}" disconnect'

    def _update_status(self):
        if 'Your VPN connection is secure'.lower() in self.output.lower():
            self.is_connected = True
        elif 'A connection already exists'.lower() in self.output.lower():
            self.is_connected = True
        else:
            self.is_connected = False
