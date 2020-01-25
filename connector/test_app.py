# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from connector import Base
from time import sleep


class TestConnector(Base):
    """
    Test GUI implementation of the Connector.
    """

    @Base.switch
    def connect(self):
        pass
        # self.gui.status_bar.update_status('Connecting...')
        # self.gui.update_idletasks()
        # sleep(5)

    @Base.switch
    def disconnect(self):
        pass
        # self.gui.status_bar.update_status('Disconnecting...')
        # self.gui.update_idletasks()
        # sleep(5)