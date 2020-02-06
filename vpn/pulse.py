# -*- coding: utf-8 -*-

"""
Provides basic interface to Pulse Secure browser based VPN: connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from vpn import VPN


class Pulse(VPN):

    _config = 'pulse.ini'
    _options = Options()
    _options.add_argument('disable-infobars')
    _options.add_argument('disable-notifications')
    _preferences = {'protocol_handler.excluded_schemes': {'pulsesecure': False}}
    _options.add_experimental_option('prefs', _preferences)
    _delay = 60
    _browser = None


    def connect(self):

        if not self._browser:

            self._browser = webdriver.Chrome(chrome_options=self._options)
            self._browser.get(getattr(self, 'portal'))

            try:
                username = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'username')))
                password = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'password')))
                submit = WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.NAME, 'btnSubmit')))
            except TimeoutException as e:
                print(e)
            else:
                username.send_keys(getattr(self, 'username'))
                password.send_keys(getattr(self, 'password'))
                submit.click()

            tries = 0

            for i in range(self._delay * 2):
                try:
                    self._browser.find_element_by_name('imgNavSignOut')
                    return True
                except Exception as e:
                    # Pulse Application Launcher not found.
                    try:
                        if tries == 0:
                            self._browser.find_element_by_link_text('Try Again').click()
                            tries += 1
                    except Exception as e:
                        pass
                    # Continue the session.
                    try:
                        self._browser.find_element_by_name('btnContinue').click()
                    except Exception as e:
                        pass
                    sleep(1)

    def disconnect(self):
        self._browser.find_element_by_name('imgNavSignOut').click()