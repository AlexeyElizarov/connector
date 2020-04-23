# -*- coding: utf-8 -*-

"""
Provides interface to desktop based VPNs.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from vpn.base import VPN
from vpn.desktop.model import Model


class Desktop(VPN):
    """
    Provides methods to connect, disconnect and close VPN using command line.
    """

    def __init__(self):
        super().__init__()
        self._model = Model(self)
        self._state = self._model.state
        self._scripts = self._model.scripts

    def connect(self):
        """
        Connect to VPN.
        :return: None
        """
        try:
            self._scripts['connect'].execute()
        except Exception as e:
            self._state.update(e)

    def disconnect(self):
        """
        Disconnect from VPN.
        :return: None
        """
        try:
            self._scripts['disconnect'].execute()
        except Exception as e:
            self._state.update(e)

    @property
    def callback(self):
        return self._state.callback
