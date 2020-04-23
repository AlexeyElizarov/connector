from webbrowser import Chrome, InternetExplorer
from helpers.ndict import ndict


DRIVERS = {'chrome': Chrome,
           'ie': InternetExplorer}


class Browser:

    def __init__(self, config):
        self._config = config
        self._webdriver = DRIVERS[self._config.get('driver').lower()](**self.options)

    @property
    def options(self):
        options = dict()
        options['binary_location'] = self.binary_location
        options['arguments'] = self.arguments
        options['extensions'] = self.extensions
        options['experimental_options'] = self.experimental_options
        options['additional_options'] = self.additional_options
        return options

    @property
    def binary_location(self):
        return self._config.get('binary_location') or ''

    @property
    def arguments(self):
        args = self._config.get('arguments', '')
        return [arg.strip() for arg in args.split(',') if args] or []

    @property
    def extensions(self):
        exts = self._config.get('extensions', '')
        return [arg.strip() for arg in exts.split(',') if exts] or []

    @property
    def experimental_options(self):
        exps = self._config.get('experimental_options') or ''
        exps = [exp.split(':') for exp in exps.split(',') if exps] or []
        return ndict(exps)

    @property
    def additional_options(self):
        opts = self._config.get('additional_options') or ''
        opts = [opt.split(':') for opt in opts.split(',') if opts] or []
        return ndict(opts)

    def open(self):
        self._webdriver.open()

    def close(self):
        self._webdriver.close()

    def get(self, url):
        self._webdriver.get(url)

    def find_by_name(self, name):
        return self._webdriver.find_by_name(name)

    def find_by_xpath(self, xpath):
        return self._webdriver.find_by_xpath(xpath)

    def find_by_id(self, id_):
        return self._webdriver.find_by_id(id_)

    def switch_to_window(self, window_id):
        self._webdriver.switch_to_window(window_id)
