# -*- coding: utf-8 -*-

"""
Provides interfaces to SAP backend system.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from subprocess import Popen
from time import sleep
from pywinauto.application import Application
from pyrfc import Connection


class SAPGUI:
    """
    This is a class for SAP GUI.
    The class provides method to open SAP GUI using command line and close SAP GUI using SAP command line.
    To use a default driver, a path to the sapshcut.exe must be added to the system PATH parameter.
    """

    # A default path to the SAP GUI driver (sapshcut.exe)
    _DEFAULT_DRIVER = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\sapshcut.exe'
    # A default path to the SAP Logon executable
    _PATH = 'saplogon.exe'

    def __init__(self, driver: str = _DEFAULT_DRIVER, config: str = ''):
        """
        The constructor for the SAPGUI class
        :param driver: a path to a sapshcut binary.
        """
        self._driver = driver
        self._app = None
        self._params = self._read_config(config)
        self._app_server = self._params.get('app_server')
        self._system = self._params.get('system')
        self._client = self._params.get('client')
        self._sysname = self._params.get('sysname')
        self._user = self._params.get('user')
        self._pw = self._params.get('pw')
        self._language = self._params.get('language')

    @property
    def _windows(self):
        """
        Returns the list of SAP GUI windows.
        :return: List of SAP GUI windows.
        """

        try:
            windows = self._app.windows(title_re='SAP Easy Access.*') + self._app.windows(title='SAP')
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
        if self._app_server:
            response = Popen("ping -n 1 " + self._app_server, shell=True)
            response.wait()
            if response.poll() == 0:
                return True
        return False

    def open(self):
        """
        Opens SAP GUI session using command line.
        :return: None
        """

        # Compose command line
        command = f'"{self._driver}" -system={self._system} -client={self._client} -sysname="{self._sysname}"'

        # If user supplied, add -user parameter to the command line
        if self._user:
            command += f' -user={self._user}'

        # If password supplied, add -pw parameter to the command line
        if self._pw:
            command += f' -pw={self._pw}'

        # If language supplied, add -language parameter to the command line
        if self._language:
            command += f' -language={self._language}'

        # Open SAP GUI instance
        Popen(command)

        # Connect to SAP GUI application instance
        self._app = Application(backend='win32').connect(path=self._PATH)

    def close(self):
        """
        Closes SAP GUI windows.
        :return: None
        """
        # If SAP application server is reachable, terminate all SAP GUI windows.
        if self.is_reachable:
            while self._windows:
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
        except:
            pass

    @staticmethod
    def _read_config(file):
        """
        Reads configuration file.
        :param file: Path to configuration file.
        :return: Dictionary of configuration parameters.
        """
        params = {}

        with open(file) as f:
            config = f.readlines()

        for line in config:
            param, value = line.split('=')
            params[param.strip()] = value.strip()

        return params


class SAPRFC:
    """
    This is a class for SAP RFC.
    The class provides method to open SAP RFC connection using SAP NetWeaver RFC Library via PyRFC implementation.
    For more information about PyRFC, please follow https://sap.github.io/PyRFC/index.html
    """

    languages = ['RU', 'EN']

    def __init__(self, profile):
        self.connection = self._connect(profile)

    @staticmethod
    def _read_profile(profile: str):
        """
        Reads connection profile. Connection parameters consist of client, user, passwd, ahost and sysnr.
        :param profile: path to SAP  connection profile.
        :return: dictionary with connection parameters
        """

        params = {}

        with open(profile, mode='r') as f:

            for param in f.readlines():
                key, value = param.split('=')
                params[key.strip()] = value.strip()

        return params

    def _connect(self, profile):
        """
        Provides connection to an SAP backend system
        :param profile: path to an SAP connection profile.
        :return: pyrfc.Connection (https://sap.github.io/PyRFC/pyrfc.html)
        """
        return Connection(**self._read_profile(profile))

    def read_table(self, query_table: str,
                   delimiter: str = '|',
                   no_data: str = '',
                   rowskips: int = 0,
                   rowcount: int = 0,
                   options: str = '',
                   fields: list = None):
        """
        Invokes RFC_READ_TABLE function module via RFC and
        processes returned data.
        :param query_table: Table to read.
        :param delimiter: Sign for indicating field limits in DATA. Default "|".
        :param no_data: If <> SPACE, only FIELDS is filled
        :param rowskips: Skips certain number of rows.
        :param rowcount: Number of rows to read.
        :param options: Selection entries, "WHERE clauses" .
        :param fields: Names (in) and structure (out) of fields to read.
        :return: tuple of data and fields
        """

        _options = [{'TEXT': options.replace('\"', '\'')}]

        if fields is None:
            _fields = []
        else:
            _fields = [{'FIELDNAME': field} for field in fields]

        response = self.connection.call('RFC_READ_TABLE',
                                        QUERY_TABLE=query_table,
                                        DELIMITER=delimiter,
                                        NO_DATA=no_data,
                                        ROWSKIPS=rowskips,
                                        ROWCOUNT=rowcount,
                                        OPTIONS=_options,
                                        FIELDS=_fields)

        _data, _fields = response['DATA'], response['FIELDS']
        _field_names = [field['FIELDNAME'] for field in _fields]

        data = list()

        if _data:
            for item in _data:
                wa = item['WA'].split('|')
                attribs = {key: value.strip() for (key, value) in zip(_field_names, wa)}
                data.append(attribs)

        fields = _fields

        return data, fields