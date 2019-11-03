# -*- coding: utf-8 -*-

"""
Implements parent class for SAP backend interface.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
from os import path
from lxml import etree


class SAP:
    """
    This a parent class for SAP backend interface.
    The class initialize SAP connection parameters from landscape description by the service name.
    """
    
    def __init__(self, service_name):

        with OpenKey(HKEY_CURRENT_USER, r'Software\SAP\SAPLogon\Options') as key:
            _config_path = QueryValueEx(key, r'PathConfigFilesLocal')[0]

        self._landscape = path.join(_config_path, 'SAPUILandscape.xml')

        tree = etree.parse(self._landscape)
        root = tree.getroot()
        service = root.xpath(f"//Service[@name='{service_name}']")[0]
        
        for key, value in service.items():
            setattr(self, key, value)
        
        

