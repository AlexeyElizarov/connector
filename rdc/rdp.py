# -*- coding: utf-8 -*-

"""
Provides interface to  RDP (Remote Desktop Protocol).
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from rdc import RDC


class RDP(RDC):

    _driver = 'mstsc.exe'
    # _config = 'rdp.ini'

    @property
    def open_command(self):
        return f'{self._driver} "{getattr(self, "rdp")}"'

    @property
    def close_command(self):
        return f'TASKKILL /F /PID {self._app.pid} /T'