# -*- coding: utf-8 -*-

"""
Provides GUI interface to SAP backend system.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from sap import SAP
from subprocess import Popen
from time import sleep
from pywinauto.application import Application
from winreg import OpenKey, QueryValueEx, HKEY_LOCAL_MACHINE


class SAPGUI(SAP):
    """
    This is a class for SAP GUI.
    The class provides method to open SAP GUI using command line and close SAP GUI using SAP command line.
    """

    # Get location of SAP Shortcut
    with OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\sapshcut.exe') as key:
        _sapshcut = QueryValueEx(key, r'')[0]

    # SAP Logon executable
    _saplogon = 'saplogon.exe'

    def __init__(self, service_name):
        """
        The constructor for the SAPGUI class
        :param service_name: Service name as it is presented in SAP Logon.
        """

        SAP.__init__(self, service_name)

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

    @property
    def is_reachable(self):
        """
        Checks if SAP application server is reachable.
        :return: Returns True if SAP application server is reachable. Else - False.
        """

        if getattr(self, 'server'):
            response = Popen("ping -n 1 " + self.hostname, shell=True)
            response.wait()
            if response.poll() == 0:
                return True
        return False

    def open(self, client: str, user: str = None, pw: str = None,  language: str = None):
        """
        Opens SAP GUI instance using command line.
        :param client: SAP backend client number
        :param user: User name
        :param pw: Password
        :param language: Logon language
        :return: None
        """

        system = getattr(self, 'server').split(':')[0]
        name = getattr(self, 'name')

        # Compose command line
        command = f'"{self._sapshcut}" -system={system} -client={client} -sysname="{name}"'

        # If user supplied, add -user parameter to the command line
        if user:
            command += f' -user={user}'

        # If password supplied, add -pw parameter to the command line
        if pw:
            command += f' -pw={pw}'
             #
        # If language supplied, add -language parameter to the command line
        if language:
            command += f' -language={language}'

        # Open SAP GUI instance
        Popen(command)

    def close(self):
        """
        Closes SAP GUI windows.
        :return: None
        """      

        # If SAP application server is reachable, terminate all SAP GUI windows.
        if self.is_reachable and not self.is_closed:
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