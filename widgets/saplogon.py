# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import ttk
from widgets import LBxSAPService
from sap import Landscape


class LFrSAPLogon(ttk.LabelFrame):
    """
    SAP Logon Widget
    """

    _padx = 2
    _pady = 2

    def __init__(self, root, node):
        ttk.LabelFrame.__init__(self, root, text='SAP Logon')

        self.services = Landscape(node).services
        self.lbl_security_id = ttk.Label(self, text='Service Name:')
        self.lbx_sap_service = LBxSAPService(self, self.services)
        self.lbx_sap_service.bind("<Double-Button-1>", self.get_service)
        self.lbx_sap_service.pack(side='left', padx=self._padx, pady=self._pady)

    def get_service(self, event):
        """
        Gets service by selected list index.
        :param event:
        :return: None
        """
        return self.services[self.lbx_sap_service.curselection()[0]]

