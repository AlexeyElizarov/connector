# -*- coding: utf-8 -*-

"""
Implements Status handling as observable.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from connector.models.observable import Observable


class Status(Observable):

    _code = -1
    _message = str

    # Status code handling
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
        self.post(self.message)

    # Message handling
    @property
    def message(self):
        return self._message

    @message.getter
    def message(self):
        if self.code < 0:
            if self.code % 2 == 0:
                return 'Disconnecting...'
            if self.code % 2 == 1:
                return 'Disconnected'
        if self.code > 0:
            if self.code % 2 == 0:
                return 'Connected'
            if self.code % 2 == 1:
                return 'Connecting...'