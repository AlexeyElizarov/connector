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
    _default_driver = r'C:\Program Files (x86)\Cisco Systems\VPN Client\vpnclient.exe'
    _default_config = None

    def __init__(self, driver=_default_driver, config=_default_config):
        VPN.__init__(self, driver, config)
        self._connect = f'"{self._driver}" connect {getattr(self, "profile")} ' \
            f'user {getattr(self, "user")} ' \
            f'pwd {getattr(self, "pwd")}'
        self._disconnect = f'"{self._driver}" disconnect'