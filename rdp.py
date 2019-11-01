# -*- coding: utf-8 -*-

"""
Implements interface to  RDP (Remote Desktop Protocol). Allows to open and close RDP from within command line.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen


class RDP:
    """ This is a class for Remote Desktop Protocol """

    # A default path to RDP
    _DEFAULT_DRIVER = 'mstsc.exe'

    def __init__(self, driver: str = _DEFAULT_DRIVER):
        """ A constructor for RDP class. """
        self._driver = driver
        self._app = None

    def open(self, rdp: str):
        """
        Opens remote desktop connection using driver and RDP connection file.
        :param rdp: a path to RDP connection file.
        :return: None.
        """
        self._app = Popen(f'{self._driver} "{rdp}"')

    def close(self):
        """ Closes remote desktop connection by process id. """
        Popen(f'TASKKILL /F /PID {self._app.pid} /T')
