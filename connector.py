"""
GUI implementation for Connectors package
"""
__author__ = 'Alexey Elizarov (alexey.elizarov@gmail.com)'
__version__ = '0.1'

from tkinter import ttk
from abc import ABC, abstractmethod


class Connector(ABC):
    """Abstract class for Connector GUI"""
    def __init__(self, root):
        self.root = root

        padx = 2
        pady = 2

        self.root.title('Connector')
        self.root.resizable(0, 0)
        self.root.minsize(300, root.winfo_height())

        self.frm_controls = ttk.Frame(root)
        self.btn_connect = ttk.Button(self.frm_controls, text='Connect')
        self.btn_disconnect = ttk.Button(self.frm_controls, text='Disconnect')
        self.btn_disconnect['state'] = 'disabled'
        self.btn_close = ttk.Button(self.frm_controls, text='Close')

        self.frm_controls.pack(expand=True, fill='x')
        self.btn_connect.pack(side='left', padx=padx, pady=pady)
        self.btn_close.pack(side='right', padx=padx, pady=pady)
        self.btn_disconnect.pack(side='right', padx=padx, pady=pady)

        self.btn_connect['command'] = self.connect
        self.btn_disconnect['command'] = self.disconnect
        self.btn_close['command'] = self.close

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    def close(self):
        try:
            self.disconnect()
        except:
            pass
        finally:
            self.root.quit()

    def switch_states(self):
        state = self.btn_connect['state']
        self.btn_connect['state'] = self.btn_disconnect['state']
        self.btn_disconnect['state'] = state


class TestGUI(Connector):
    def connect(self):
        print('connect')

    def disconnect(self):
        print('disconnect')