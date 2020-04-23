# -*- coding: utf-8 -*-

"""
Provides basic interface to FortiClient: open, close, connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from time import sleep
from vpn import WebBased
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class FortiClient(WebBased):
    """
    Provides basic interface to FortiClient.
    """

    _config = 'forticlient.ini'
    _options = Options()
    _options.binary_location = r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe'
    _options.add_argument('--remote-debugging-port=12345')
    _options.add_argument('--b')

    @WebBased.open
    def connect(self):
        """
        Connects to VPN with given VPN name, user and password.
        :return: None
        """

        self._browser.find_element_by_id('vpn-sidebar').click()

        try:
            WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.ID, 'vpn-connection-info')))
        except TimeoutException as e:
            print(type(e), e)
        else:

            for i in range(5):
                try:
                    vpn_conn = self._browser.find_element_by_id('vpn-connection')
                    vpn_name = Select(vpn_conn)
                    vpn_name.select_by_visible_text(getattr(self, 'vpn_name'))
                except ElementNotInteractableException as e:
                    print(type(e), e)
                    sleep(1)

            username = self._browser.find_element_by_id('vpn-username')
            username.clear()
            username.send_keys(getattr(self, 'username'))
            password = self._browser.find_element_by_id('vpn-password')
            password.send_keys(getattr(self, 'password'))
            sleep(1)
            self._browser.find_element_by_id('vpn-connect-button').click()

    @WebBased.close
    def disconnect(self):
        """
        Disconnects from VPN.
        :return: None
        """
        try:
            self._browser.find_element_by_id('vpn-disconnect-button').click()
        except Exception as e:
            print(type(e), e)


