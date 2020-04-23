# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import ttk

from app.widgets import PADX, PADY
from app.widgets.sap_service_list import LBxSAPService


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
        self.lbx_sap_services.focus_set()
        self.lbx_sap_services.select_set(0)

    @property
    def selected_service(self):
        return self.services[self.lbx_sap_services.curselection()[0]]







