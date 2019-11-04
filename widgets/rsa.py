from tkinter import ttk


class LFrRSA(ttk.LabelFrame):
    """
    Implements RSA Security feature.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        ttk.LabelFrame.__init__(self, root, text='RSA')

        self.lbl_security_id = ttk.Label(self, text='Security ID:')
        self.ent_security_id = ttk.Entry(self, width=6)

        self.lbl_security_id.pack(side='left', padx=self._padx, pady=self._pady)
        self.ent_security_id.pack(side='left', padx=self._padx, pady=self._pady)