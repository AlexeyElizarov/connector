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
        """
        Connects to VPN if VPN object provided and opens RDC.
        :return: None
        """

        try:
            self.model.vpn.connect()
        except Exception as e:
            print(type(e), e)

        try:
            self.model.rdc.open()
        except Exception as e:
            print(type(e), e)

    @Controller.switch
    def disconnect(self):
        """
        Closes RDC and disconnects from VPN if object VPN provided.
        :return: None
        """

        # Try to close RDC
        try:
            self.model.rdc.close()
        except Exception as e:
            print(type(e), e)

        # Try to disconnect from VPN
        try:
            self.model.vpn.disconnect()
        except Exception as e:
            print(type(e), e)

    def close(self):
        """
        Disconnects and closes application.
        :return: None
        """

        try:
            self.disconnect()
        except Exception as e:
            print(e)
        finally:
            self.quit()