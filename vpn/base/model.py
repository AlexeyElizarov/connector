# -*- coding: utf-8 -*-

"""
Implements parent base VPN data model
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from os.path import join
from configparser import ConfigParser
from vpn.base.state import State
from vpn.base.credentials import Credentials


class Model:
    """
    This is a parent class for VPN clients.
    This class provides interfaces to data model for VPN clients.
    """

    def __init__(self, controller):

        self.controller = controller
        self.state = State()
        self.config = ConfigParser()
        self.config.read(join(self.controller.dirname, 'config.ini'))
        self.credentials = Credentials()



