# -*- coding: utf-8 -*-

"""
Provides base API to browser.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webbrowser.error import ErrorHandler
from webbrowser.exceptions import InvalidCertificate


class Browser:
    """
    Requirements:
    - must provide API to Chrome
    - must provide API to IE
    - it must be possible to open browser
    - it must be possible to close browser
    - it must be possible to pass options to Chrome
    - it must be possible to pass options to IE
    - it must be possible to handle errors while getting url
    - it must be possible to find web elements
    - it must be possible to interact with web elements
    """

    _webdriver = None
    _options = None
    _session = None
    _error_handler = ErrorHandler()
    _delay = 60

    def open(self):
        """
        Open browser session.
        :return:
        """
        self._session = self._webdriver(options=self._options)

    def close(self):
        """
        Close browser session
        :return:
        """
        self._session.quit()

    def get(self, url):
        """
        Get url and resolve exceptions if any.
        :param url:
        :return:
        """

        try:
            self._get(url)
        except InvalidCertificate:
            self._override()

    def switch_to_window(self, window_id):
        try:
            self._switch_to_window(window_id)
        except InvalidCertificate:
            self._override()

    def find_by_name(self, name):
        """
        Find webelement by name waiting until presence of element located on the webpage.
        :param name: name of the element
        :return: Selenium webelement object

        """
        try:
            return WebDriverWait(self._session, self._delay).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutException:
            raise

    def find_by_xpath(self, xpath):
        """
        Find webelement by xpath waiting until presence of element located on the webpage.
        :param name: name of the element
        :return: Selenium webelement object

        """
        try:
            return WebDriverWait(self._session, self._delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise

    def find_by_id(self, id_):
        """
        Find webelement by ID waiting until presence of element located on the webpage.
        :param name: id of the element
        :return: Selenium webelement object

        """
        try:
            return WebDriverWait(self._session, self._delay).until(EC.presence_of_element_located((By.ID, id_)))
        except TimeoutException:
            raise

    @ErrorHandler.check
    def _get(self, url):
        self._session.get(url)
        self._error_handler.register(self._session)

    @ErrorHandler.check
    def _switch_to_window(self, window_id):
        self._session.switch_to.window(self._session.window_handles[window_id])
        self._error_handler.register(self._session)

    def _override(self):
        pass






