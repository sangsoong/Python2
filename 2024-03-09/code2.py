class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
        print(f'{name} was born')
    
    def __del__(self):
        Person.population -= 1
        print(f'{self.name} was dead')

    @classmethod
    def get_population(cls):
        return cls.population

p1 = Person('kim')
p2 = Person('lee')
p3 = Person('park')
print(Person.get_population())
del p1
del p2
print(Person.get_population())