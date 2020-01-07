# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import ttk
from connector.widgets.sap_service_list import LBxSAPService
from connector.widgets import PADX, PADY


class LFrSAPLogon(ttk.LabelFrame):
    """
    SAP Logon Widget
    """

    def __init__(self, root, services):
        super().__init__(root, text='SAP Logon')

        self.root = root
        self.services = services
        self.lbx_sap_services = LBxSAPService(self, self.services)
        self.lbx_sap_services.pack(side='left', padx=PADX, pady=PADY)

    @property
    def selected_service(self):
        return self.services[self.lbx_sap_services.curselection()[0]]





