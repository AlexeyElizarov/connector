from tkinter import ttk


class FrmOptions(ttk.Frame):
    """
    Implements manager to display optional parameters for connection.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        ttk.Frame.__init__(self, root)

        self.controls = root.controls