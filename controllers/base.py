# -*- coding: utf-8 -*-

"""
Implements base controller class
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

from widgets import GUI
import webbrowser


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = GUI(self)

    def open_url(self, event):
        webbrowser.open_new(self.model.app.access_url)

    @staticmethod
    def switch(func):
        def switcher(*args):
            self = args[0]
            self.model.status.code *= -1
            func(self)
            self.view.controls.switch()
            self.model.status.code += 1
        return switcher

    def run(self):
        self.view.mainloop()

    def quit(self):
        self.view.quit()