class Mentor:
    def __init__(self, name):
        self.name = name
        # self.junior = False
    def info(self):
        return 'hello', self.name

class InfoAge(Mentor):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def info(self):
        return f'{self.age} years old'

class InfoExperience(Mentor):
    def __init__(self, name, experience):
        super().__init__(name)
        self.experience = experience
    def info(self):
        return f'Опыт работы: {self.experience} лет '

a = Mentor('Askat')
print(a.info())
b = InfoAge('Askan', 25)
print(b.info())
c = InfoExperience('Askan', 4)
print(c.info())
print(c.info)

class A:
    def __init__(self, name):
        self.name = name
    def info(self):
        return 'hello', self.name