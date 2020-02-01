# -*- coding: utf-8 -*-

"""
Implements SAP Logon based Connector.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from connector.controllers.base import Connector
from time import sleep


class SAPLogon(Connector):

    _sap = None
    _vpn = None

    @property
    def sap(self):
        return self._sap

    @sap.setter
    def sap(self, value):
        self.model.sap = value
        self._sap = self.model.sap
        self.gui.saplogon()
        self.gui.saplogon.lbx_sap_services.bind('<<ListboxSelect>>', self._select_service)
        self.gui.saplogon.lbx_sap_services.bind('<Double-Button-1>', self._connect)
        self.gui.unbind('<Return>')
        self.gui.saplogon.lbx_sap_services.bind('<Return>', self._connect)

    def _connect(self, event):
        self._select_service(event)
        self.connect()

    @property
    def vpn(self):
        return self._vpn

    @vpn.setter
    def vpn(self, value):
        self.model.vpn = value
        self._vpn = self.model.vpn

    def _select_service(self, event):
        """
        Updates selected SAP service.
        :param event: None
        :return: None
        """

        # Update selected service
        self.sap.selected_service = self.gui.saplogon.selected_service

        # Enable connect button if service is selected.
        if self.sap.selected_service:
            self.gui.controls.btn_connect['state'] = 'normal'
        else:
            self.gui.controls.btn_connect['state'] = 'disabled'

    def connect(self):
        """
        Connects to VPN and opens SAP GUI session.
        :return: None.
        """

        if self.model.status.code < 0:
            self.model.status.code *= -1
        else:
            self.model.status.code += 1

        # If saprouter has not been provided, connect to VPN and open SAP GUI.
        if not getattr(self.sap.selected_service, 'routerid', None):

            # Check if application server is reachable. If it is not, then connect to VPN.
            if not self.sap.selected_service.is_reachable:
                self.vpn.connect()

            # Check over time if application server is reachable. If it is, then open SAP GUI.
            for i in range(15):
                if self.sap.selected_service.is_reachable:
                    self.sap.selected_service.gui.open()
                    self.sap.connections.append(self.sap.selected_service)
                    break
                else:
                    sleep(1)

        # Else, open SAP GUI.
        else:
            self.sap.selected_service.gui.open()
            self.sap.connections.append(self.sap.selected_service)

        # Check over time if SAP GUI is opened.
        for i in range(20):
            if not self.sap.selected_service.gui.is_closed:
                self.gui.controls.btn_disconnect['state'] = 'normal'
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
            for service in self.sap.connections:
                if not service.gui.is_closed:
                    service.gui.close()

        try:
            self.vpn.disconnect()
        except:
            pass
        self.gui.controls.btn_disconnect['state'] = 'disabled'
        # self.model.status.post('Disconnected')
        self.model.status.code = -1




