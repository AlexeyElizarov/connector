# -*- coding: utf-8 -*-

"""
Provides basic interface to Pulse Secure browser based VPN: connect, disconnect
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from vpn import WebBased


class Pulse(WebBased):

    _config = 'pulse.ini'
    _options = Options()
    _options.add_argument('disable-infobars')
    _options.add_argument('disable-notifications')
    _preferences = {'protocol_handler.excluded_schemes': {'pulsesecure': False}}
    _options.add_experimental_option('prefs', _preferences)
    _delay = 60
    _webdriver = None

    @WebBased.open
    def connect(self):

        try:
            ent_username = WebDriverWait(self._webdriver, self._delay).until(EC.presence_of_element_located((By.NAME, 'username')))
            ent_password = WebDriverWait(self._webdriver, self._delay).until(EC.presence_of_element_located((By.NAME, 'password')))
            btn_submit = WebDriverWait(self._webdriver, self._delay).until(EC.presence_of_element_located((By.NAME, 'btnSubmit')))
        except TimeoutException as e:
            print(e)
        else:
            ent_username.send_keys(getattr(self, 'username'))
            ent_password.send_keys(getattr(self, 'password'))
            btn_submit.click()

        tries = 0

        for i in range(self._delay * 2):
            try:
                self._webdriver.find_element_by_name('imgNavSignOut')
                return True
            except Exception as e:
                # Pulse Application Launcher not found.
                try:
                    if tries == 0:
                        self._webdriver.find_element_by_link_text('Try Again').click()
                        tries += 1
                except Exception as e:
                    pass
                # Continue the session.
                try:
                    self._webdriver.find_element_by_name('btnContinue').click()
                except Exception as e:
                    pass
                sleep(1)

    @WebBased.close
    def disconnect(self):

        if self.is_connected:
            self._webdriver.find_element_by_name('imgNavSignOut').click()