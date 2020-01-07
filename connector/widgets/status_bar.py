from tkinter import ttk, GROOVE
from connector.widgets import PADX, PADY


class FrmStatusBar(ttk.Frame):
    """
    Implements status bar widgets
    """

    def __init__(self, root):
        ttk.Frame.__init__(self, root, relief=GROOVE)

        self.lbl_message = ttk.Label(self)
        self.lbl_message.pack(padx=PADX, pady=PADY, side='left')

    def update_(self, text):
        self.lbl_message['text'] = text
