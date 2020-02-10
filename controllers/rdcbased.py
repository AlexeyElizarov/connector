# -*- coding: utf-8 -*-

"""
Implements Baseline controller
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from controllers import Controller


class RDCBased(Controller):

    def _connect(self, event):
        # Connect if connection button is not disabled.
        if not str(self.view.controls.btn_connect['state']) == 'disabled':
            self.connect()

    @Controller.switch
    def connect(self):
        self.model.rdc.open()

    @Controller.switch
    def disconnect(self):
        self.model.rdc.close()

    def close(self):
        """
        Disconnects and closes application.
        :return: None
        """

        if self.model.is_connected:
            try:
                self.disconnect()
            except Exception as e:
                print(e)

        self.quit()