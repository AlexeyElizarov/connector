from subprocess import Popen

class RDP:
    """ This is a wrapper class for Remote Desktop Protocol """

    # A default path to RDP
    _DEFAULT_DRIVER = 'mstsc.exe'

    def __init__(self, driver: str = _DEFAULT_DRIVER):
        """ A constructor for RDP class. """
        self._driver = driver
        self._app = None

    def open(self, rdp: str):
        """
        Opens remote desktop connection using driver and RDP connection file.
        :param rdp: a path to RDP connection file.
        :return: None.
        """
        self._app = Popen(f'{self._driver} "{rdp}"')

    def close(self):
        """ Closes remote desktop connection by process id. """
        Popen(f'TASKKILL /F /PID {self._app.pid} /T')