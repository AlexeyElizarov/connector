# -*- coding: utf-8 -*-

"""
Implements VPN driver data model.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


class Driver:

    def __init__(self, config):
        self._config = config

        for key, value in self._config.items():
            setattr(self, key, value)
