# -*- coding: utf-8 -*-

"""
Provides interface to webbased based VPNs.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from vpn.base import VPN
from vpn.webbased.model import Model


class Webbased(VPN):
    """
    Provides methods to connect, disconnect and close VPN using command line.
    """

    def __init__(self):
        super().__init__()
        self._model = Model(self)
        self._state = self._model.state
        self.browser = self._model.browser
        self.portal = self._model.credentials

    def connect(self):
        """
        Connect to VPN.
        :return: None
        """
        pass

    def disconnect(self):
        """
        Disconnect from VPN.
        :return: None
        """
        pass

    @staticmethod
    def open(func):
        def wrapped(*args):
            self = args[0]
            self.browser.open()
            func(self)
        return wrapped

    @staticmethod
    def close(func):
        def wrapped(*args):
            self = args[0]
            func(self)
            self.browser.close()
        return wrapped

    @property
    def callback(self):
        return self._state.callback
