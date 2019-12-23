# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from sap import Landscape


class ConnectorModel:
    """
    the Model manages the data and defines rules and behaviors of the Connector.
    """

    def __init__(self, **options):

        for key, value in options.items():
            setattr(self, key, value)

        if getattr(self, 'sap', None):
            setattr(self, 'sap_services', Landscape(getattr(self, 'sap')).services)
