class Dog:
    animal_type = "mammals"
    number = 3
    is_hungry = True

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def number_of_dogs(self):
        return 'I have {} dogs'.format(self.number)

    def animal_species(self):
        return 'And they are all {}, of course'.format(self.animal_type)

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

    def walk(self):
        return '{} is walking'.format(self.name)


class Pets(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def description(self):
        return '{} is {}'.format(self.name, self.age)

    def walk(self):
        return f'{super().walk()}'


# dog instances
tom = Pets('Tom', 6)
fletcher = Pets('Fletcher', 7)
larry = Pets('Larry', 9)

dogs = []
dogs.append(tom)
dogs.append(fletcher)
dogs.append(larry)

# dog inheritance

print(tom.number_of_dogs())
print(tom.description())
print(fletcher.description())
print(larry.description())
print(tom.animal_species())

# hungry dogs fed


def feed():
    for dog in dogs:
        dog.eat()

    return fletcher.is_hungry


if feed() is True:
    print('My dogs are hungry')

else:
    print('My dogs are not hungry')