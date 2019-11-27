# -*- coding: utf-8 -*-

"""
Provides interface to  Teamviewer via command line.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen


class Teamviewer:
    """
    This is a class for Teamviewer
    The class allows to open and close Teamviewer from within command line.
    """

    # A default path to Teamviewer
    # A path to teamviewer.exe
    _DEFAULT_DRIVER = r'C:\Program Files (x86)\TeamViewer\TeamViewer.exe'

    def __init__(self, driver: str = _DEFAULT_DRIVER):
        """ A constructor for Teamviewer class. """
        self._driver = driver
        self._app = None

    def open(self, id: str, password: str):
        """
        Opens Teamviewer session with given partner ID and password.
        :param rdp: a path to RDP connection file.
        :return: None.
        """

        command = f'{self._driver} --id {id} --Password {password}'
        print(command)
        self._app = Popen(f'{self._driver} --id {id} --Password {password}')

    def close(self):
        """ Closes remote desktop connection by process id. """
        Popen(f'TASKKILL /F /PID {self._app.pid} /T')
