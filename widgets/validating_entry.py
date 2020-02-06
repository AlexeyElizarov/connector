# -*- coding: utf-8 -*-

"""
This module implements a validating version of the Tkinter Entry widget.
Taken from http://effbot.org/zone/tkinter-entry-validate.htm
"""

from abc import abstractmethod
from tkinter import ttk, StringVar


class EntValidating(ttk.Entry):
    # base class for validating entry widgets

    def __init__(self, master, value='', **kw):
        ttk.Entry.__init__(self, master, **kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace('w', self.__callback)
        self.config(textvariable=self.__variable)
        self.newvalue = None

    def __callback(self, *dummy):

        value = self.__variable.get()
        newvalue = self.validate(value)

        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(self.newvalue)
        else:
            self.__value = value

    @abstractmethod
    def validate(self, value):
        # override: return value, new value, or None if invalid
        return value