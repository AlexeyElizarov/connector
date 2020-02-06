# -*- coding: utf-8 -*-

"""
Implements class for SAP backend interface.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from configparser import ConfigParser

from sap import Landscape


class SAP:
    """
    This a class for SAP backend interface.
    The class initializes SAP connection parameters from landscape description by the service name and config file.
    The main purpose of the class is to handle SAP connection parameters.
    """

    _config = 'sap.ini'

    def __init__(self, node):
        """
        Initializes SAP backend connection parameters 
        :param service_name: Service node as it is presented in SAP Logon.
        """

        self._saplogon = Landscape(node)
        self._parse_config()
        self.connections = []

    def _parse_config(self):
        config = ConfigParser()
        config.read(self._config)

        for service in self.services:

            service_name = service.name
            if service.name.endswith(']'):
                service_name = service.name[:-1]

            try:
                service.client = config[service_name]['client']
                service.user = config[service_name]['user']
                service.password = config[service_name]['password']

                if config[service_name]['language']:
                    service.language = config[service_name]['language']
                else:
                    service.language = config['DEFAULT']['language']

            except Exception as e:
                pass

    @property
    def services(self):
        """
        Returns list of SAP Logon services.
        :return:
        """
        return self._saplogon.services

    def get_service_by_name(self, service_name):
        """
        Return service by name from self.services.
        :param service_name: service name.
        :return: service object from self.services.
        """

        for service in self.services:
            if service.name == service_name:
                return service