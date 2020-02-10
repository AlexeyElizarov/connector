# -*- coding: utf-8 -*-

"""
Implements Connector base class.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from models.model import Model
from controllers import RDCBased, SAPLogon


class Connector:

    def __init__(self):
        self.model = Model(self)

        if self.model.app.layout == 'sap':
            self.controller = SAPLogon(self.model)
        elif self.model.app.layout == 'default':
            self.controller = RDCBased(self.model)

        self.controller.run()

