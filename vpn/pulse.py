# -*- coding: utf-8 -*-

"""
Provides basic interface to Pulse Secure browser based VPN: connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from vpn import VPN


class Pulse(VPN):

    options = Options()
    options.add_argument('disable-infobars')
    options.add_argument('disable-notifications')
    preferences = {'protocol_handler.excluded_schemes': {'pulsesecure': False}}
    options.add_experimental_option('prefs', preferences)
    browser = None

    def connect(self):

        if not self.browser:
            self.browser = webdriver.Chrome(chrome_options=self.options)
            self.browser.get(getattr(self, 'portal'))

        for i in range(30):
            try:
                self.browser.find_element_by_name('username').send_keys(getattr(self, 'username'))
                self.browser.find_element_by_name('password').send_keys(getattr(self, 'password'))
            except Exception as e:
                print(e)
                sleep(1)
                continue
            else:
                self.browser.find_element_by_name('btnSubmit').click()

    def disconnect(self):
        self.browser.find_element_by_name('imgNavSignOut').click()