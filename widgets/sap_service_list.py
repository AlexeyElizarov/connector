# -*- coding: utf-8 -*-

"""
Implements SAP Service List Box
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from tkinter import Listbox, END


class LBxSAPService(Listbox):
    """
    Implements SAP Service List Box.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root, services: list = None):
        Listbox.__init__(self, root, width=50)

        if services:
            for service in services:
                self.insert(END, service.name)

