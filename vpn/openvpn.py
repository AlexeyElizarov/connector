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
    _default_driver = 'openvpn-gui'
    _default_config = None

    def __init__(self, driver=_default_driver, config=_default_config):
        VPN.__init__(self, driver, config)
        self._connect = f'"{self._driver}" --connect {getattr(self, "config")}'
        self._disconnect = ['taskkill.exe /F /IM openvpn.exe',
                            'taskkill.exe /F /IM openvpn-gui.exe']

