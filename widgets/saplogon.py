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
        super().__init__(root, text='SAP Logon')

        self.root = root
        self.services = Landscape(node).services
        self.lbx_sap_services = LBxSAPService(self, self.services)
        self.lbx_sap_services.pack(side='left', padx=self._padx, pady=self._pady)

    @property
    def selected_service(self):
        return self.services[self.lbx_sap_services.curselection()[0]]





