from tkinter import ttk
from connector.widgets.rsa import LFrRSA
from connector.widgets.saplogon import LFrSAPLogon


class FrmOptions(ttk.Frame):
    """
    Implements manager to display optional parameters for connection.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root, model):
        ttk.Frame.__init__(self, root)

        self.root = root

        if getattr(model, 'rsa', None):
            self.rsa = LFrRSA(self)
            self.rsa.pack(expand=True, fill='x', padx=self._padx, pady=self._pady)

        if getattr(model, 'sap', None):
            self.saplogon = LFrSAPLogon(self, getattr(model, 'sap_services'))
            self.saplogon.pack(expand=True, fill='x', padx=self._padx, pady=self._pady)