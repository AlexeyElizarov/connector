
# -*- coding: utf-8 -*-

"""
Provides basic interface to Check Point browser based VPN: connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import WebBased
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep


class CheckPoint(WebBased):

    _config = 'checkpoint.ini'
    _webdriver = webdriver.Ie
    _delay = 60
    _ssl_network_extender = None

    @WebBased.open
    def connect(self):

        # Sign in to customer portal
        try:
            ent_username = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'userName')))
            ent_password = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'loginInput')))
            btn_submit = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'Login')))
        except TimeoutException as e:
            print(e)
        else:
            ent_username.send_keys(getattr(self, 'username'))
            ent_password.send_keys(getattr(self, 'password'))
            btn_submit.click()

        # Connect to VPN
        try:
            btn_connect = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Connect"]')))
        except TimeoutException as e:
            print(e)
        else:
            btn_connect.click()

        sleep(5)

        # Handle security issues with SSL Network Extender
        try:
            self._browser.switch_to.window(self._browser.window_handles[1])
            self._browser.get('javascript:document.getElementById("overridelink").click();')
        except Exception as e:
            print(type(e), e)
        finally:
            self._browser.switch_to.window(self._browser.window_handles[0])


    @WebBased.close
    def disconnect(self):

        # Log out from Araymond Mobile Access
        self._browser.switch_to.window(self._browser.window_handles[0])
        actions = webdriver.ActionChains(self._browser)
        logout = self._browser.find_element_by_id('LogOutTD')
        actions.move_to_element(logout).click(logout).perform()

        # Sign out from Araymond Mobile Access
        sleep(2)
        signout = self._browser.find_element_by_id('doSignOut')
        signout.click()

    def _update_status(self):

        try:
            WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Disconnect"]')))
        except TimeoutException as e:
            print(e)
        else:
            self.is_connected = True
