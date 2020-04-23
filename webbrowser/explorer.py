# -*- coding: utf-8 -*-

"""
Provides API to Internet Explorer.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from selenium.webdriver import Ie as Webdriver
from selenium.webdriver.ie.options import Options
from webbrowser import Browser
from webbrowser.exceptions import InvalidCertificate


class InternetExplorer(Browser):

    _webdriver = Webdriver
    _options = Options()

    def __init__(self, **options):
        """
        Initialize IE browser session with options provided.
        :param options:
        """

        [self._options.add_argument(arg) for arg in options.get('arguments', [])]
        [self._options.add_additional_option(name, opt) for name, opt in options.get('additional_options', {}).items()]

    def _override(self):
        """
        Overrides link in case of certain exceptions.
        :return:
        """

        try:
            self._session.get('javascript:document.getElementById("overridelink").click();')
        except Exception as e:
            print(type(e), e)