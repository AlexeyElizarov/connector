# -*- coding: utf-8 -*-

"""
Implements base VPN controller
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn.base.model import Model
from os.path import dirname
from inspect import getfile


class Controller:

    def __init__(self):
        self.model = Model(self)

    @property
    def dirname(self):
        return dirname(getfile(self.__class__))

