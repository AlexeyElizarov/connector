# -*- coding: utf-8 -*-

"""
Abstract GUI implementation for custom connectors
"""

__author__ = 'Alexey Elizarov (alexey.elizarov@gmail.com)'


from tkinter import ttk
from abc import ABC, abstractmethod


class Connector(ABC):
    """
    Abstract class for Connector GUI
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        self.root = root

        self.root.title('Connector')
        self.root.resizable(0, 0)
        self.root.minsize(300, root.winfo_height())

        self.frm_controls = ttk.Frame(root)
        self.btn_connect = ttk.Button(self.frm_controls, text='Connect')
        self.btn_disconnect = ttk.Button(self.frm_controls, text='Disconnect')
        self.btn_disconnect['state'] = 'disabled'
        self.btn_close = ttk.Button(self.frm_controls, text='Close')

        self.frm_controls.pack(expand=True, fill='x')
        self.btn_connect.pack(side='left', padx=self._padx, pady=self._pady)
        self.btn_close.pack(side='right', padx=self._padx, pady=self._pady)
        self.btn_disconnect.pack(side='right', padx=self._padx, pady=self._pady)

        self.btn_connect['command'] = self.connect
        self.btn_disconnect['command'] = self.disconnect
        self.btn_close['command'] = self.close

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
        except:
            pass
        finally:
            self.root.quit()

    def switch_states(self):
        """
        Switches states of the Connect button.
        :return: None
        """
        state = self.btn_connect['state']
        self.btn_connect['state'] = self.btn_disconnect['state']
        self.btn_disconnect['state'] = state


class TestGUI(Connector):
    """
    Test GUI implementation of the Connector.
    """
    def connect(self):
        print('connect')

    def disconnect(self):
        print('disconnect')
