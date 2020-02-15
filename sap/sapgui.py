# -*- coding: utf-8 -*-

"""
Provides GUI interface to SAP backend system.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen
from time import sleep
from winreg import OpenKey, QueryValueEx, HKEY_LOCAL_MACHINE

from pywinauto.application import Application


class SAPGUI:
    """
    This is a class for SAP GUI.
    The main purpose of the class is to handle SAP GUI for a given SAP service.
    The class provides method to open SAP GUI using command line and close SAP GUI using SAP command line.
    """

    # Get location of SAP Shortcut
    with OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\sapshcut.exe') as key:
        _sapshcut = QueryValueEx(key, r'')[0]

    # SAP Logon executable
    _saplogon = 'saplogon.exe'

    def __init__(self, service):
        self.service = service

    @property
    def _app(self):
        """
        # Connection to SAP GUI application instance
        :return: Connection to SAP GUI application instance
        """
        try:
            return Application(backend='win32').connect(path=self._saplogon)
        except Exception:
            return None

    @property
    def _windows(self):
        """
        Returns the list of SAP GUI windows.
        :return: List of SAP GUI windows.
        """

        try:
            windows = self._app.windows(class_name='SAP_FRONTEND_SESSION')
            return windows
        except:
            return []

    @property
    def is_closed(self):
        """
        Checks if there are any SAP GUI windows opened.
        :return: Returns True when there're no SAP GUI windows open. Else - False.
        """
        if self._windows:
            return False
        else:
            return True

    def open(self):
        """
        Opens SAP GUI instance using command line.
        :return: None
        """

        # Compose command line
        command = f'"{self._sapshcut}" -system={self.service.systemid} -client={self.service.client} -sysname="{self.service.name}"'

        # If user supplied, add -user parameter to the command line
        if getattr(self.service, 'user', None):
            command += f' -user={self.service.user}'

        # If password supplied, add -pw parameter to the command line
        if getattr(self.service, 'password', None):
            command += f' -pw={self.service.password}'

        # If language supplied, add -language parameter to the command line
        if getattr(self.service, 'language', None):
            command += f' -language={self.service.language}'

        # Open SAP GUI instance
        Popen(command)

    def close(self):
        """
        Closes SAP GUI windows.
        :return: None
        """      

        # If SAP application server is reachable, terminate all SAP GUI windows.
        if not self.is_closed:
            while not self.is_closed:
                for window in self._windows:
                    self._terminate(window.handle)

    def _terminate(self, handle):
        """
        Tries to terminate SAP GUI window by its handle.
        :param handle: SAP GUI window handle.
        :return: None
        """
        try:
            edit = self._app.window(handle=handle).window(class_name='Edit')
            edit.type_keys('/nex')
            edit.type_keys('{ENTER}')
            sleep(1)
        except Exception:
            pass