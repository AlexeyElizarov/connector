# -*- coding: utf-8 -*-

"""
Abstract GUI implementation for custom connectors
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


# TODO: add RSA Security GUI feature
# TODO: - limit security id entry - number of chars
# TODO: - limit security id entry - only numerical
# TODO: add log GUI feature
# TODO: implement ttk styles for padding

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

        self.options = FrmOptions(self.root, **options)
        self.controls = FrmControls(self.root)

        self.options.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')

        self.controls.btn_connect['command'] = self.connect
        self.controls.btn_disconnect['command'] = self.disconnect
        self.controls.btn_close['command'] = self.close


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


class TestGUI(Connector):
    """
    Test GUI implementation of the Connector.
    """
    def connect(self):
        print('connect')
        self.controls.switch()

    def disconnect(self):
        print('disconnect')
        self.controls.switch()
