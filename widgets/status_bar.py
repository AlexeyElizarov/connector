from tkinter import ttk, GROOVE, StringVar
from widgets import PADX, PADY


class FrmStatusBar(ttk.Frame):
    """
    Implements status bar widgets
    """

    def __init__(self, root):
        ttk.Frame.__init__(self, root, relief=GROOVE)

        self.message = StringVar()
        self.lbl_message = ttk.Label(self, textvariable=self.message)
        self.lbl_message.pack(padx=PADX, pady=PADY, side='left')

    def refresh(self, message):
        self.message.set(message)
        self.update_idletasks()
