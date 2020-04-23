# -*- coding: utf-8 -*-

"""
Implements desktop based VPN data model
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from os import listdir
from os.path import join, splitext
from vpn.base.model import Model as Base
from vpn.base.shell import Shell
from vpn.base.driver import Driver
from vpn.base.script import Script


class Model(Base):
    """
    This is a parent class for VPN clients.
    This class provides interfaces to data model for VPN clients.
    """

    def __init__(self, controller):
        super().__init__(controller)
        self.shell = Shell(self.config['SHELL'])
        self.shell.register(self.state)
        self.driver = Driver(self.config['DRIVER'])
        self.scripts = {}

        scripts_path = join(self.controller.dirname, 'scripts')

        for script in listdir(scripts_path):
            self.scripts[splitext(script)[0]] = Script(script=join(scripts_path, script), **vars(self))






