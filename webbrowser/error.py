from webbrowser.exceptions import InvalidCertificate
from selenium.common.exceptions import NoSuchElementException

EXCEPTIONS = {'DLG_FLAGS_INVALID_CA': InvalidCertificate}


class ErrorHandler:

    _session = None

    @staticmethod
    def check(func):
        def wrapped(*args):
            self = args[0]
            func(*args)
            self._error_handler.handle()
        return wrapped

    def register(self, session):
        self._session = session

    def handle(self):

        try:
            error_code = self._session.find_element_by_id('ErrorCode').get_attribute('innerHTML')
        except NoSuchElementException:
            return
        else:
            for exception in EXCEPTIONS:
                if exception in error_code:
                    raise EXCEPTIONS[exception]