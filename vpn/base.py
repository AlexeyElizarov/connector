# -*- coding: utf-8 -*-

"""
Implements parent class for VPN clients
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from configparser import ConfigParser


class VPN:
    """
    This is a parent class for VPN clients.
    This class provides methods to read configuration settings from .ini file (model).
    """

    _config = None  # A path to configuration file

    def __init__(self):
        config = ConfigParser()
        config.read(self._config)

        for key, value in config['DEFAULT'].items():
            setattr(self, key, value)