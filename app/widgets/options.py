from tkinter import ttk


class FrmOptions(ttk.Frame):
    """
    Implements manager to display optional parameters for connection.
    """

    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.controls = root.controls
