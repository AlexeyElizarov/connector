# -*- coding: utf-8 -*-

"""
Implements VPN credentials data model.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from configparser import ConfigParser


class Credentials:
    """
    Provides interface to VPN Credentials configuration file.
    """
    def __init__(self):

        config = ConfigParser()
        config.read('vpn.ini')

        for key, value in config.items('DEFAULT'):
            setattr(self, key, value)
