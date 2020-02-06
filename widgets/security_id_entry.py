# -*- coding: utf-8 -*-

"""
Implements RSA Security feature.
Taken from http://effbot.org/zone/tkinter-entry-validate.htm
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from widgets.validating_entry import EntValidating


class EntSecurityId(EntValidating):

    def __init__(self, root, value: str = None, maxlength: int = None, **kw):
        EntValidating.__init__(self, root, **kw)
        self.controls = root.controls
        self.maxlength = maxlength

    def validate(self, value):
        """
        Validates value of the Validating Entry.
        :param value: Value to validate
        :return: validated value or None
        """

        if self.maxlength is None or len(value) <= self.maxlength:
            if value[-1:] in '0123456789':
                if len(value) == self.maxlength:
                    self.controls.btn_connect['state'] = 'enabled'

                else:
                    self.controls.btn_connect['state'] = 'disabled'
                return value

        # if len(value) == self.maxlength:

