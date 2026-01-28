class Mentor:
    def __init__(self, name):
        self.name = name
        self.junior = False

    def info(self):
        return f'{self.name} junior' if self.junior else f'{self.name}'