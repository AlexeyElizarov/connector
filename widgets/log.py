# -*- coding: utf-8 -*-

"""
Log Frame widget provides user interface to a logger.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from widgets.logger import TextHandler
import logging


class FrmLog(ttk.Frame):
    """
    Implements Logging widget to output processing log.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        ttk.Frame.__init__(self, root)

        self.stx_log = ScrolledText(self, state='disabled')
        self.stx_log.configure(font='TkFixedFont')
        self.stx_log.pack(padx=self._padx, pady=self._pady)
