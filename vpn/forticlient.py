# -*- coding: utf-8 -*-

"""
Provides basic interface to FortiClient: open, close, connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep


class FortiClient:
    """
    Provides basic interface to FortiClient.
    """

    _default_driver = r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe'

    def __init__(self):
        self._app = None
        self._is_connected = False
        self._chrome_options = Options()
        self._chrome_options.binary_location = self._default_driver
        self._chrome_options.add_argument('--remote-debugging-port=12345')

    def open(self):
        """
        Opens FortiClient.
        :return: None
        """
        if not self._app:
            self._app = webdriver.Chrome(chrome_options=self._chrome_options)

    def close(self):
        """
        Closes FortiClient.
        :return: None
        """
        if self._app:
            self._app.quit()
            del self._app

    def connect(self, vpn_name, username, password):
        """
        Connects to VPN with given VPN name, user and password.
        :param vpn_name: VPN name
        :param username: username
        :param password: password
        :return:
        """

        self._app.find_element_by_id('vpn-sidebar').click()

        for i in range(5):
            try:
                vpn_names = Select(self._app.find_element_by_id('vpn-connection'))
                vpn_names.select_by_visible_text(vpn_name)
                username_input = self._app.find_element_by_id('vpn-username')
                username_input.clear()
                username_input.send_keys(username)
                self._app.find_element_by_id('vpn-password').send_keys(password)
            except Exception as e:
                print(e)
                sleep(i)
                continue
            else:
                self._app.find_element_by_id('vpn-connect-button').click()
                self._is_connected = True
                break

    def disconnect(self):
        """
        Disconnects from VPN.
        :return:
        """
        if self._is_connected:
            self._app.find_element_by_id('vpn-disconnect-button').click()

