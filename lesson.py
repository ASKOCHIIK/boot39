class Mentor:
    def __init__(self, name, age):
        self.name = name
        self.senior = False
        self.__age = age


    def info(self):
        return 'hello', self.name

    def get_age(self):
        return self.__age

class Level(Mentor):
    def lvl(self):
        self.senior = True
        return 'you are now senior mentor'

a = Mentor('Askat', 25)
print(a.get_age())









