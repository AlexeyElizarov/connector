# -*- coding: utf-8 -*-

"""
Implements interface to OpenVPN client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN


class OpenVPN(VPN):
    """
    Implements interface to OpenVPN client.
    """
    # Default Open VPN client
    _default_driver = 'openvpn-gui'

    def __init__(self, _default_driver, config):
        VPN.__init__(self, _default_driver, config)
        self._connect = f'"{self._driver}" --connect {getattr(self, "config")}'
        self._disconnect = ['taskkill.exe /F /IM openvpn.exe',
                            'taskkill.exe /F /IM openvpn-gui.exe']

