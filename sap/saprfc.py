# -*- coding: utf-8 -*-

"""
Provides RFC interface to SAP backend system.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from pyrfc import Connection
from sap import SAP


class SAPRFC(SAP):
    """
    This is a class for SAP RFC.
    The class provides method to open SAP RFC connection using SAP NetWeaver RFC Library via PyRFC implementation.
    For more information about PyRFC, please follow https://sap.github.io/PyRFC/index.html
    """

    def __init__(self, service_name):
        SAP.__init__(self, service_name)

    def connect(self, client: str, user: str = None, pw: str = None,  language: str = None):
        """
        Returns Connection object to an SAP backend system
        :param client: SAP backend client number
        :param user: User name
        :param pw: Password
        :param language: Logon language
        :return: pyrfc.Connection (https://sap.github.io/PyRFC/pyrfc.html)
        """

        params = dict(client=client, user=user, passwd=pw, lang=language, ashost=self.hostname, sysnr=self.sysnr)

        return Connection(**params)

