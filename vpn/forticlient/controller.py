# -*- coding: utf-8 -*-

"""
Provides basic interface to FortiClient.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from vpn import Webbased


class FortiClient(Webbased):

    @Webbased.open
    def connect(self):

        sidebar = self.browser.find_by_id('vpn-sidebar')
        sidebar.click()


    @Webbased.close
    def disconnect(self):
        """
        Disconnects from VPN.
        :return: None
        """
        pass