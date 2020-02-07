# -*- coding: utf-8 -*-
"""
Implements Access Page widget that allows user to open access url in webbrowser
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter.ttk import Frame, Label
from tkinter import RIGHT
from widgets import PADX, PADY


class FrmAccess(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.lbl_access = Label(self, text='View access page', foreground='blue', cursor='hand2')
        self.lbl_access.pack(side=RIGHT, padx=PADX, pady=PADY)
        self.lbl_access.bind('<Button-1>', self.controller.open_url)
