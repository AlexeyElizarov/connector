# -*- coding: utf-8 -*-

"""
Implements class for SAP backend interface.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from sap import Landscape


class SAP:
    """
    This a class for SAP backend interface.
    The class initializes SAP connection parameters from landscape description by the service name and config file.
    The main purpose of the class is to handle SAP connection parameters.
    """

    def __init__(self, node):
        """
        Initializes SAP backend connection parameters 
        :param service_name: Service node as it is presented in SAP Logon.
        """

        self._saplogon = Landscape(node)
        self.connections = []

    @property
    def services(self):
        """
        Returns list of SAP Logon services.
        :return:
        """
        return self._saplogon.services

    def config(self, file: str = ''):
        """
        Updates SAP Logon services with parameters from the configuration file.
        :param file:  A path to SAP service config file.
        :return: None
        """

        config = self._read_config(file)

        for service in self.services:
            service_config = config.get(service.name, dict())
            service.client = service_config.get('client', None)
            service.user = service_config.get('user', None)
            service.password = service_config.get('password', None)

    def get_service_by_name(self, service_name):
        """
        Return service by name from self.services.
        :param service_name: service name.
        :return: service object from self.services.
        """

        for service in self.services:
            if service.name == service_name:
                return service

    @staticmethod
    def _read_config(file: str = ''):
        """
        Reads connection configuration parameters from the file.
        :param file: a path to the connection config file.
        :return: config dictionary
        """
        config = dict()
        node = None

        with open(file, 'r') as f:
            config_file = f.readlines()

        for line in config_file:
            if line.startswith('['):
                node = line.strip()[1:-1]
                config[node] = dict()
            else:
                param, value = line.split('=')
                if node:
                    config[node][param.strip()] = value.strip()
                else:
                    config[param.strip()] = value.strip()

        return config
