from tkinter import ttk, SUNKEN, FLAT, RIDGE, GROOVE


class FrmStatusBar(ttk.Frame):
    """
    Implements status bar widgets
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        ttk.Frame.__init__(self, root, relief=GROOVE)

        self.lbl_message = ttk.Label(self)
        self.lbl_message.pack(padx=self._padx, pady=self._pady, side='left')

    def update_(self, text):
        self.lbl_message['text'] = text
