# -*- coding: utf-8 -*-

"""
Provides interface to Cisco VPN Client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN


class Cisco(VPN):
    """
    Provides interface to Cisco VPN Client.
    """
    # Default Cisco VPN Driver
    _driver = r'C:\Program Files (x86)\Cisco Systems\VPN Client\vpnclient.exe'
    _config = 'cisco.ini'

    @property
    def connect_command(self):
        return f'"{self._driver}" connect {getattr(self, "profile")} '\
            f'user {getattr(self, "user")} ' \
            f'pwd {getattr(self, "pwd")}'

    @property
    def disconnect_command(self):
        return f'"{self._driver}" disconnect'