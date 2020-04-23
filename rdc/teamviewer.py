# -*- coding: utf-8 -*-

"""
Provides interface to  Teamviewer via command line.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from rdc import RDC


class Teamviewer(RDC):
    """
    This is a class for Teamviewer
    The class allows to open and close Teamviewer from within command line.
    """

    # A default path to Teamviewer
    _driver = r'C:\Program Files (x86)\TeamViewer\TeamViewer.exe'
    # _config = 'teamviewer.ini'

    @property
    def open_command(self):
        return f'"{self._driver}" --id {getattr(self, "id")} --Password {getattr(self, "password")}'

    @property
    def close_command(self):
        return f'TASKKILL /F /PID {self._app.pid} /T'