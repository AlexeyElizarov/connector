# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import Tk

from widgets import FrmOptions, FrmControls, FrmStatusBar, LFrSAPLogon, LFrRSA, PADX, PADY


class GUI(Tk):
    """
    GUI for the Connector App. The sole function of this class is to draw GUI and catch events.
    """

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        # Main loop settings
        x = int(self.winfo_screenwidth() / 2 - 150)
        y = int(self.winfo_screenheight() / 2 - 150)
        self.title(self.controller.model.app.title)
        self.resizable(0, 0)
        self.minsize(300, self.winfo_height())
        self.geometry(f'+{x}+{y}')

        # Initialization of widgets
        self.controls = FrmControls(self)
        self.options = FrmOptions(self)
        self.status_bar = FrmStatusBar(self)
        self.controller.model.status.register(self.status_bar)
        self.controller.model.status.code = -1

        if self.controller.model.app.layout == 'sap':
            self._saplogon_layout()
        elif self.controller.model.app.layout == 'rsa':
            self._rsa_layout()

        # Geometry management
        self.options.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')
        self.status_bar.pack(expand=True, fill='x', padx=PADX, pady=PADY)

        # Default bindings
        self.controls.btn_connect['command'] = self.controller.connect
        if not self.controller.model.app.layout == 'sap':
            self.bind('<Return>', self.controller._connect)
        self.controls.btn_disconnect['command'] = self.controller.disconnect
        self.controls.btn_close['command'] = self.controller.close

    def _saplogon_layout(self):
        """
        Initializes SAPLogon layout.
        :return: None
        """
        self.saplogon = LFrSAPLogon(self.options, self.controller.model.sap.services)
        self.saplogon.pack(expand=True, fill='x', padx=PADX, pady=PADY)
        if not self.saplogon.selected_service:
            self.controls.btn_connect['state'] = 'disabled'

        # Bindings
        self.saplogon.lbx_sap_services.bind('<<ListboxSelect>>', self.controller._select_service)
        self.saplogon.lbx_sap_services.bind('<Double-Button-1>', self.controller._connect)
        self.saplogon.lbx_sap_services.bind('<Return>', self.controller._connect)

    def _rsa_layout(self):
        """
         Initializes RSA layout.
         :return: None
         """
        self.rsa = LFrRSA(self.options)
        self.rsa.pack(expand=True, fill='x', padx=PADX, pady=PADY)

    def run(self):
        self.mainloop()
