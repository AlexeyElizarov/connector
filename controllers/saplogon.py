# -*- coding: utf-8 -*-

"""
Implements SAP Logon based Connector.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from time import sleep

from controllers.base import Controller


class SAPLogon(Controller):

    def select_service(self, event):
        """
        Updates selected SAP service.
        :param event: None
        :return: None
        """

        # Update selected service
        self.model.sap.selected_service = self.view.saplogon.selected_service

        # Enable connect button if service is selected.
        if self.model.sap.selected_service:
            self.view.controls.btn_connect['state'] = 'normal'
        else:
            self.view.controls.btn_connect['state'] = 'disabled'

    def connect(self, event=None):
        """
        Connects to VPN and opens SAP GUI session.
        :return: None.
        """

        self.select_service(event)

        if self.model.status.code < 0:
            self.model.status.code *= -1
        else:
            self.model.status.code += 1

        # If VPN service provided, connect to VPN first.
        if getattr(self.model, 'vpn', None):

            # Check if application server is reachable. If it is not, then connect to VPN.
            if not self.model.sap.selected_service.is_reachable:
                self.model.vpn.connect()

            # Check over time if application server is reachable. If it is, then open SAP GUI.
            for i in range(30):
                if self.model.sap.selected_service.is_reachable:
                    self.model.sap.selected_service.gui.open()
                    self.model.sap.connections.append(self.model.sap.selected_service)
                    break
                else:
                    sleep(1)

        # Else, open SAP GUI.
        else:
            self.model.sap.selected_service.gui.open()
            self.model.sap.connections.append(self.model.sap.selected_service)

        # Check over time if SAP GUI is opened.
        for i in range(20):
            if not self.model.sap.selected_service.gui.is_closed:
                self.view.controls.btn_disconnect['state'] = 'normal'
                self.model.status.code += 1
                break
            else:
                sleep(1)

    def disconnect(self):
        """
        Closes SAP GUI sessions and disconnects from VPN.
        :return: None
        """

        # self.model.status.post('Disconnecting...')
        self.model.status.code *= -1

        for i in range(15):
            for service in self.model.sap.connections:
                if not service.gui.is_closed:
                    service.gui.close()

        try:
            self.model.vpn.disconnect()
        except:
            pass
        self.view.controls.btn_disconnect['state'] = 'disabled'
        # self.model.status.post('Disconnected')
        self.model.status.code = -1

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


