# -*- coding: utf-8 -*-

"""
Provides RFC interface to SAP backend system.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from pyrfc import Connection


class SAPRFC:
    """
    This is a class for SAP RFC.
    The class provides method to open SAP RFC connection using SAP NetWeaver RFC Library via PyRFC implementation.
    For more information about PyRFC, please follow https://sap.github.io/PyRFC/index.html
    """

    def __init__(self, service):
        self.service = service

    def connect(self):
        """
        Returns Connection object to an SAP backend system
        :param client: SAP backend client number
        :param user: User name
        :param pw: Password
        :param language: Logon language
        :return: pyrfc.Connection (https://sap.github.io/PyRFC/pyrfc.html)
        """

        params = dict(client=self.service.client, user=self.service.user, passwd=self.service.password,
                      lang=self.service.language, ashost=self.service.hostname, sysnr=self.service.sysnr)

        return Connection(**params)

