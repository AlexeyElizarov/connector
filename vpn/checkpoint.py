
# -*- coding: utf-8 -*-

"""
Provides basic interface to Check Point browser based VPN: connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from vpn import VPN
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep


class CheckPoint(VPN):

    _config = 'checkpoint.ini'
    _browser = webdriver.Ie()
    _delay = 60

    def connect(self):

        if not self._browser:

            try:
                username = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'userName')))
                password = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'loginInput')))
                submit = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'Login')))
            except TimeoutException as e:
                print(e)
            else:
                username.send_keys(getattr(self, 'username'))
                password.send_keys(getattr(self, 'password'))
                submit.click()

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

        # Quite browser
        self._browser.quit()

