# -*- coding: utf-8 -*-

"""
Provides interface to SAP Landscape settings
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
from subprocess import Popen
from os import path
from lxml import etree
from sap import GUI, RFC


class SAPLandscape:
    """
    Provides interface to SAP Landscape settings parsed from SAPUILandscape.xml.
    """

    # Get location of SAP UI Landscape
    with OpenKey(HKEY_CURRENT_USER, r'Software\SAP\SAPLogon\Options') as key:
        _config_path = QueryValueEx(key, r'PathConfigFilesLocal')[0]
        _landscape = path.join(_config_path, 'SAPUILandscape.xml')

    def __init__(self, node_name):

        # Get node by using node name and set class attributes.
        tree = etree.parse(self._landscape)
        root = tree.getroot()
        node = Node(root.xpath(f"//Node[@name='{node_name}']")[0])
        self.services = []

        # Get SAP services using their IDs.
        for item in node.items:
            service = Service(root.xpath(f"//Service[@uuid='{getattr(item, 'serviceid')}']")[0])
            self.services.append(service)


class Element:
    """
    Parent class for an XML element.
    """
    def __init__(self, node):
        for key, value in node.items():
            setattr(self, key, value)


class Node(Element):
    """
    Class for SAP Logon Node.
    """
    def __init__(self, node):
        super().__init__(node)

        # Get node items
        self.items = [Item(item) for item in node.findall('.//Item')]


class Item(Element):
    """
    Class for SAP Logon node item.
    """
    pass


class Service(Element):
    """
    Class for SAP services.
    """
    def __init__(self, node):
        super().__init__(node)

        self.hostname, self.port = getattr(self, 'server').split(':')
        self.sysnr = self.port[2:]

        self.gui = GUI(self)
        self.rfc = RFC(self)

    @property
    def is_reachable(self):
        """
        Checks if SAP application server is reachable.
        :return: Returns True if SAP application server is reachable. Else - False.
        """

        if getattr(self, 'server'):
            response = Popen("ping -n 1 " + self.hostname, shell=True)
            response.wait()
            if response.poll() == 0:
                return True
        return False
