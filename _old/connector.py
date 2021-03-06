# -*- coding: utf-8 -*-

"""
Abstract GUI implementation for custom connectors
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from tkinter import Tk
from abc import ABC, abstractmethod
from widgets import FrmControls, FrmOptions


class Connector(ABC):
    """
    Abstract class for Connector GUI
    """

    _padx = 2
    _pady = 2

    def __init__(self, **options):
        self.root = Tk()

        self.root.title('Connector')
        self.root.resizable(0, 0)
        self.root.minsize(300, self.root.winfo_height())

        # Initialization of widgets
        self.options = FrmOptions(self.root, **options)
        self.controls = FrmControls(self.root)

        # Geometry management
        self.options.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')

        # Commands and bindings
        self.controls.btn_connect['command'] = self.connect
        self.controls.btn_disconnect['command'] = self.disconnect
        self.controls.btn_close['command'] = self.close

        if options.get('saplogon'):
            self.options.saplogon.lbx_sap_services.bind('<Double-Button-1>', self._connect)
        elif options.get('rsa'):
            pass
            self.root.after(250, self.check_rsa_key)
        else:
            self.root.bind('<Return>', self._connect)

    def check_rsa_key(self):
        # print('checking rsa')
        rsa_key = self.options.rsa.ent_security_id.get()
        if len(rsa_key) == 6:
            self.controls.btn_connect['state'] = 'enabled'
            self.root.bind('<Return>', self._connect)
        else:
            self.controls.btn_connect['state'] = 'disabled'
            self.root.unbind('<Return>')

        self.root.after(250, self.check_rsa_key)

    def _connect(self, event):
        self.connect()

    @staticmethod
    def switch(func):
        def switcher(*args):
            self = args[0]
            func(self)
            self.controls.switch()
        return switcher

    @abstractmethod
    def connect(self):
        """
        Abstract method to connect.
        :return: None
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Abstract method to disconnect.
        :return: None
        """
        pass

    def close(self):
        """
        Disconnects and closes application.
        :return: None
        """
        try:
            self.disconnect()
        except Exception:
            pass
        finally:
            self.root.quit()

    def run(self):
        self.root.mainloop()

    @staticmethod
    def read_config(file: str = ''):
        """
        Reads connection configuration parameters from the file.
        :param file: a path to the connection config file.
        :return: config dictionary
        """
        config = dict()
        node = None

        with open(file, 'r') as f:
            config_file = f.readlines()

        for line in config_file:
            if line.startswith('['):
                node = line.strip()[1:-1]
                config[node] = dict()
            else:
                param, value = line.split('=')
                if node:
                    config[node][param.strip()] = value.strip()
                else:
                    config[param.strip()] = value.strip()

        return config


class TestGUI(Connector):
    """
    Test GUI implementation of the Connector.
    """

    @Connector.switch
    def connect(self):
        pass

    @Connector.switch
    def disconnect(self):
        pass
