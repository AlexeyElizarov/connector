class State:

    callback = ''

    def update(self, message):
        self.callback = message

    def clear(self):
        self.callback = ''


