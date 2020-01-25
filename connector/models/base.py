# -*- coding: utf-8 -*-

"""
Implements Connector data model.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from sap import SAP
from connector.models import Observable


class ConnectorModel:
    """
    the Model manages the data and defines rules and behaviors of the Connector.
    """

    _title = None  # Application title
    _sap = None  # SAP landscape object
    _vpn = None  # VPN object
    _status = Observable()  # Status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status._code = value
        self._status.post(self._status._code)

    # Application title handling
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @title.getter
    def title(self):
        if self._title:
            return self._title
        else:
            return 'Connector'

    # SAP Landscape handling
    @property
    def sap(self):
        return self._sap

    @sap.setter
    def sap(self, value):
        self._sap = SAP(value)

