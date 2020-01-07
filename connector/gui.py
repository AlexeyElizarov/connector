# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import Tk
from connector.widgets import FrmOptions, FrmControls, FrmStatusBar, LFrSAPLogon, LFrRSA, PADX, PADY


class ConnectorGUI(Tk):
    """
    GUI for the Connector App. The sole function of this class is to draw GUI.
    """

    def __init__(self, model):
        super().__init__()

        self.model = model
        self.title(self.model.title)
        self.resizable(0, 0)
        self.minsize(300, self.winfo_height())

        # Initialization of widgets
        self.controls = FrmControls(self)
        self.options = FrmOptions(self)
        self.status_bar = FrmStatusBar(self)

        # Geometry management
        self.options.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')
        self.status_bar.pack(expand=True, fill='x', padx=PADX, pady=PADY)

    def saplogon(self):
        self.saplogon = LFrSAPLogon(self.options, self.model.sap.services)
        self.saplogon.pack(expand=True, fill='x', padx=PADX, pady=PADY)

    def rsa(self):
        self.rsa = LFrRSA(self.options)
        self.rsa.pack(expand=True, fill='x', padx=PADX, pady=PADY)

    def run(self):
        self.mainloop()
