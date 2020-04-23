# -*- coding: utf-8 -*-

"""
Implements Connector data model.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from configparser import ConfigParser
from app.models import App, Status, VPN, RDC
from sap import SAP


class Model:
    """
    the Model manages the data and defines rules and behaviors of the Connector.
    """

    _config = 'config.ini'
    status = Status()  # Status observable object

    def __init__(self, controller):
        self.controller = controller

        config = ConfigParser()
        config.read(self._config)

        # App default settings
        self.app = App(**config['DEFAULT'])

        # RDC handling
        if self.app.rdc:
            self.rdc = RDC[self.app.rdc.lower()]()

        # SAP landscape handling
        if self.app.sap:
            self.sap = SAP(self.app.sap)

        # VPN handling
        if self.app.vpn:
            self.vpn = VPN[self.app.vpn.lower()]()

    @property
    def is_connected(self):
        if self.status.code > 0 and self.status.code % 2 == 0:
            return True
        return False
