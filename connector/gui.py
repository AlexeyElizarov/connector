# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import Tk
from connector.widgets import FrmOptions, FrmControls


class ConnectorGUI(Tk):
    """
    GUI for the Connector App. The sole function of this class is to draw GUI.
    """

    def __init__(self, model):
        super().__init__()

        self.title('Connector')
        self.resizable(0, 0)
        self.minsize(300, self.winfo_height())

        # Initialization of widgets
        self.options = FrmOptions(self, model)
        self.controls = FrmControls(self)

        # Geometry management
        self.options.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')

    def run(self):
        self.mainloop()
