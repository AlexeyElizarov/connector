# -*- coding: utf-8 -*-

"""
Implements class for application data model.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


class App:

    title = 'Connector'
    rdc = None
    sap = None
    vpn = None
    rsa = False
    access_url = None

    def __init__(self, **params):
        for item, value in params.items():
            setattr(self, item, value)

    @property
    def layout(self):
        """
        App layout depending on .sap or .rsa attributes.
        :return:
        """
        if self.sap:
            return 'sap'
        if self.rsa:
            return 'rsa'
        return 'default'






