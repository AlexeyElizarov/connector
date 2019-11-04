# -*- coding: utf-8 -*-

"""
Abstract GUI implementation for custom connectors
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


# TODO: add RSA Security GUI feature
# TODO: - limit security id entry - number of chars
# TODO: - limit security id entry - only numerical
# TODO: add log GUI feature

from tkinter import ttk
from tkinter import Tk
from abc import ABC, abstractmethod


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

        self.frm_options = ttk.Frame(self.root)
        self.frm_controls = ttk.Frame(self.root)
        self.btn_connect = ttk.Button(self.frm_controls, text='Connect')
        self.btn_disconnect = ttk.Button(self.frm_controls, text='Disconnect')
        self.btn_disconnect['state'] = 'disabled'
        self.btn_close = ttk.Button(self.frm_controls, text='Close')

        self.frm_options.pack(expand=True, fill='x')
        self.frm_controls.pack(expand=True, fill='x')
        self.btn_connect.pack(side='left', padx=self._padx, pady=self._pady)
        self.btn_close.pack(side='right', padx=self._padx, pady=self._pady)
        self.btn_disconnect.pack(side='right', padx=self._padx, pady=self._pady)

        self.btn_connect['command'] = self.connect
        self.btn_disconnect['command'] = self.disconnect
        self.btn_close['command'] = self.close

        try:
            if options['rsa']:
                self.lfr_rsa = ttk.LabelFrame(self.frm_options, text='RSA', height=100)
                self.lbl_security_id = ttk.Label(self.lfr_rsa, text='Security ID:')
                self.ent_security_id = ttk.Entry(self.lfr_rsa, width=6)
                self.lfr_rsa.pack(expand=True, fill='x', padx=self._padx, pady=self._pady)
                self.lbl_security_id.pack(side='left', padx=self._padx, pady=self._pady)
                self.ent_security_id.pack(side='left', padx=self._padx, pady=self._pady)
        except KeyError:
            pass


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

    def switch_states(self):
        """
        Switches states of the Connect button.
        :return: None
        """
        state = self.btn_connect['state']
        self.btn_connect['state'] = self.btn_disconnect['state']
        self.btn_disconnect['state'] = state

    def run(self):
        self.root.mainloop()


class TestGUI(Connector):
    """
    Test GUI implementation of the Connector.
    """
    def connect(self):
        print('connect')
        self.switch_states()

    def disconnect(self):
        print('disconnect')
        self.switch_states()
