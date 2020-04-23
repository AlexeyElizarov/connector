# -*- coding: utf-8 -*-

"""
Implements RSA Security feature.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import ttk

from app.widgets import PADX, PADY
from app.widgets.security_id_entry import EntSecurityId


class LFrRSA(ttk.LabelFrame):
    """
    Implements RSA Security feature.
    """

    def __init__(self, root):
        ttk.LabelFrame.__init__(self, root, text='RSA')

        self.controls = root.controls
        self.controls.btn_connect['state'] = 'disabled'

        self.lbl_security_id = ttk.Label(self, text='Security ID:')
        self.ent_security_id = EntSecurityId(self, maxlength=6, width=6)

        self.lbl_security_id.pack(side='left', padx=PADX, pady=PADY)
        self.ent_security_id.pack(side='left', padx=PADX, pady=PADY)

