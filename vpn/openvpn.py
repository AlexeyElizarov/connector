# -*- coding: utf-8 -*-

"""
Provides interface to OpenVPN client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import Desktop


class OpenVPN(Desktop):
    """
    Provides interface to OpenVPN client.
    """

    _driver = 'openvpn-gui'
    _config = 'openvpn.ini'

    @property
    def connect_command(self):
        return f'"{self._driver}" --connect {getattr(self, "profile")}'

    @property
    def disconnect_command(self):
        return ['taskkill.exe /F /IM openvpn.exe',
                'taskkill.exe /F /IM openvpn-gui.exe']
