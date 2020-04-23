# -*- coding: utf-8 -*-

"""
Provides interface to Open VPN Client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import Desktop


class OpenVPN(Desktop):

    def close(self):
        """
        Close VPN client.
        :return: None
        """
        try:
            self._scripts['close'].execute()
        except Exception as e:
            self._state.update(e)