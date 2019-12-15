# -*- coding: utf-8 -*-

"""
Provides interface to SAP Landscape settings
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
from os import path
from lxml import etree


class SAPLandscape:
    """
    Provides interface to SAP Landscape settings.
    """

    # Get location of SAP UI Landscape
    with OpenKey(HKEY_CURRENT_USER, r'Software\SAP\SAPLogon\Options') as key:
        _config_path = QueryValueEx(key, r'PathConfigFilesLocal')[0]
        _landscape = path.join(_config_path, 'SAPUILandscape.xml')

    def __init__(self, node_name):

        # Get node by using noe name and set class attributes.
        tree = etree.parse(self._landscape)
        root = tree.getroot()
        self.node = Node(root.xpath(f"//Node[@name='{node_name}']")[0])
        self.services = []

        for item in self.node.items:
            service = Service(root.xpath(f"//Service[@uuid='{getattr(item, 'serviceid')}']")[0])
            self.services.append(service)


class Node:
    def __init__(self, node):

        for key, value in node.items():
            setattr(self, key, value)

        self.items = [Item(item) for item in node.findall('.//Item')]


class Item:
    def __init__(self, item):

        for key, value in item.items():
            setattr(self, key, value)


class Service:
    def __init__(self, service):
        for key, value in service.items():
            setattr(self, key, value)

        self.hostname, self.port = getattr(self, 'server').split(':')
        self.sysnr = self.port[2:]