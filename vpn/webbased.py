# -*- coding: utf-8 -*-

"""
Provides base interface to web based VPNs
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN
from abc import abstractmethod
from selenium import webdriver


class WebBased(VPN):

    _browser = None
    _webdriver = webdriver.Chrome  # Chrome is webdriver by default
    _options = None
    _delay = 60
    is_connected = False

    @staticmethod
    def close(func):
        def wrapped(*args):
            self = args[0]
            func(self)
            if self._browser:
                self._browser.quit()
                del self._browser
                self.is_connected = False
        return wrapped

    @staticmethod
    def open(func):
        def wrapped(*args):
            self = args[0]
            if not self._browser:
                if self._options:
                    self._browser = self._webdriver(chrome_options=self._options)
                else:
                    self._webdriver = self._webdriver()
                if getattr(self, 'portal', None):
                    self._webdriver.get(self.portal)
            func(self)
            self.is_connected = True
        return wrapped

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


