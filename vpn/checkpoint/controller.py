# -*- coding: utf-8 -*-

"""
Provides interface to Cisco VPN Client.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import Webbased


class Checkpoint(Webbased):

    def connect(self):

        # Open browser
        self.browser.open()

        # Get portal
        self.browser.get(self.portal.url)

        # Sign in
        username = self.browser.find_by_name('userName')
        username.send_keys(self.portal.username)
        password = self.browser.find_by_name('loginInput')
        password.send_keys(self.portal.password)
        submit = self.browser.find_by_name('Login')
        submit.click()

        # Connect to VPN
        connect = self.browser.find_by_xpath('//input[@value="Connect"]')
        connect.click()

        # Handle security issues with SSL Network Extender
        self.browser.switch_to_window(1)
        self.browser.switch_to_window(0)

    def disconnect(self):

        # Disconnect from VPN
        logout = self.browser.find_by_id('LogOutTD')
        logout.click()

        # Log out
        signout = self.browser.find_by_id('doSignOut')
        signout.click()

        # Close browser
        self.browser.close()