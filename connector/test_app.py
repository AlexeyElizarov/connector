# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from connector import Base


class TestConnector(Base):
    """
    Test GUI implementation of the Connector.
    """

    @Base.switch
    def connect(self):
        self.gui.status_bar.update_('Connecting...')

    @Base.switch
    def disconnect(self):
        self.gui.status_bar.update_('Disconnecting...')