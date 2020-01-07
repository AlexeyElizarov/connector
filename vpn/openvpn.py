# -*- coding: utf-8 -*-

"""
Provides interface to OpenVPN client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN


class OpenVPN(VPN):
    """
    Provides interface to OpenVPN client.
    """
    # Default Open VPN client
    _driver = 'openvpn-gui'

    @property
    def connect_command(self):
        return f'"{self._driver}" --connect {getattr(self, "profile")}'

    @property
    def disconnect_command(self):
        return ['taskkill.exe /F /IM openvpn.exe',
                'taskkill.exe /F /IM openvpn-gui.exe']
