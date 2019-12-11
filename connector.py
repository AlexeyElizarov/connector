# -*- coding: utf-8 -*-

"""
Abstract GUI implementation for custom connectors
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

# TODO: implement ttk styles for padding
# TODO: add SAP service selection feature
# TODO: connect by ENTER
# TODO: RSA - disable connect (raise pop-up) if security key is not entered.

from tkinter import Tk
from abc import ABC, abstractmethod
from widgets import FrmControls, FrmOptions
# from widgets import FrmLog, TextHandler
import logging
from time import sleep
import threading


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
        # self.log = FrmLog(self.root)
        self.controls = FrmControls(self.root)

        self.options.pack(expand=True, fill='x')
        # self.log.pack(expand=True, fill='x')
        self.controls.pack(expand=True, fill='x')

        self.controls.btn_connect['command'] = self.connect
        self.controls.btn_disconnect['command'] = self.disconnect
        self.controls.btn_close['command'] = self.close

        self.log_threads = []

        # # Create textLogger
        # text_handler = TextHandler(self.log.stx_log)
        #
        # # Logging configuration
        # logging.basicConfig(filename='test.log',
        #                     level=logging.INFO,
        #                     format='%(asctime)s - %(levelname)s - %(message)s')
        #
        # # Add the handler to logger
        # logger = logging.getLogger()
        # logger.addHandler(text_handler)

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
        # self.t1 = threading.Thread(target=self.connect, args=[])
        # self.t2 = threading.Thread(target=self.disconnect, args=[])
        # for thread in self.log_threads:
        #     thread.start()

        # self.t1.start()
        # self.t2.start()
        self.root.mainloop()

        # for thread in self.log_threads:
        #     thread.join()

        # self.t1.join()
        # self.t2.join()


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

    # def connect(self):
    #     t1 = threading.Thread(target=self.connect, args=[])
    #     self.log_threads.append(t1)
    #     logging.info('Connecting')
    #
    #     sleep(3)
    #     self.controls.switch()
    #     logging.info('Connected')
    #
    # def disconnect(self):
    #     t2 = threading.Thread(target=self.disconnect, args=[])
    #     self.log_threads.append(t2)
    #     logging.info('Disconnect')
    #     sleep(3)
    #     self.controls.switch()
