# -*- coding: utf-8 -*-

"""
Provides interface to Barracuda VPN client.

-c : Connect
-d : Disconnect
-a : Local password
(-aa : Prompt for local password: automatically ask
-h : Hide vpn.exe (not visible)
-n : profile name
-p : password (server)
(-pp : Automatic VPN Client password prompt
-r : Profile (Registry ID)
-u : User

"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from vpn import Desktop


class Barracuda(Desktop):
    """
    Provides interface to Barracuda VPN client.
    """

    _driver = r'C:\Program Files\BarracudaNG\vpn.exe'
    _config = 'barracuda.ini'

    @property
    def _connect_command(self):
        return f'"{self._driver}" -u {getattr(self, "user")} -p {getattr(self, "password")}'

    @property
    def _disconnect_command(self):
        return f'"{self._driver}" -d'

    def _update_status(self):
        print(self.output)
