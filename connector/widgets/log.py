# -*- coding: utf-8 -*-

"""
Log Frame widget provides user interface to a logger.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from connector.widgets.logger import TextHandler
from connector.widgets import PADX, PADY
import logging


class FrmLog(ttk.Frame):
    """
    Implements Logging widget to output processing log.
    """

    def __init__(self, root):
        ttk.Frame.__init__(self, root)

        self.stx_log = ScrolledText(self, state='disabled')
        self.stx_log.configure(font='TkFixedFont')
        self.stx_log.pack(padx=PADX, pady=PADY)
