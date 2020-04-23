from selenium.webdriver import Chrome as Webdriver
from selenium.webdriver.chrome.options import Options
from webbrowser import Browser


class Chrome(Browser):

    _webdriver = Webdriver
    _options = Options()

    def __init__(self, **options):

        self._options.binary_location = options.get('binary_location', '') or ''
        [self._options.add_argument(arg) for arg in options.get('arguments', [])]
        [self._options.add_extension(ext) for ext in options.get('extensions', [])]
        [self._options.add_experimental_option(name, opt) for name, opt in options.get('experimental_options', {}).items()]

    # def find_element_by_id(self, id_):
    #     # print(type(self._session))
    #     self._session.find_element_by_id(id_)

    def navigate(self, url):
        self._session.get(url)

