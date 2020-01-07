"""
Implements RSA based Connector.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from connector.controllers.base import Connector


class RSA(Connector):

    def __init__(self, title):
        super().__init__(title)
        self.gui.rsa()