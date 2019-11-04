from tkinter import ttk


class FrmControls(ttk.Frame):
    """
    Implements GUI controls to connect to customer's system, disconnect from customer's system and close application.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root):
        ttk.Frame.__init__(self, root)

        self.btn_connect = ttk.Button(self, text='Connect')
        self.btn_disconnect = ttk.Button(self, text='Disconnect')
        self.btn_disconnect['state'] = 'disabled'
        self.btn_close = ttk.Button(self, text='Close')

        self.btn_connect.pack(side='left', padx=self._padx, pady=self._pady)
        self.btn_close.pack(side='right', padx=self._padx, pady=self._pady)
        self.btn_disconnect.pack(side='right', padx=self._padx, pady=self._pady)

    def switch(self):
        """
        Switches states of the connection buttons.
        :return: None
        """
        state = self.btn_connect['state']
        self.btn_connect['state'] = self.btn_disconnect['state']
        self.btn_disconnect['state'] = state

