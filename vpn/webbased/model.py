# -*- coding: utf-8 -*-

"""
Implements web-based VPN data model
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from vpn.base.model import Model as Base
from vpn.base.browser import Browser
from vpn.base.credentials import Credentials


class Model(Base):
    """
    This is a parent class for VPN clients.
    This class provides interfaces to data model for VPN clients.
    """

    def __init__(self, controller):
        super().__init__(controller)
        self.browser = Browser(self.config['BROWSER'])
        self.credentials = Credentials()




