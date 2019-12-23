# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from connector import Connector


class TestConnector(Connector):
    """
    Test GUI implementation of the Connector.
    """

    @Connector.switch
    def connect(self):
        pass

    @Connector.switch
    def disconnect(self):
        pass