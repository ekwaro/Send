from pets_class import Pets
pets = []
tom = Pets('Tom', 17)
fletcher = Pets('Fletcher', 5)
larry = Pets('Larry', 20)
pets.append(tom)
pets.append(fletcher)
pets.append(larry)

for pet in pets:
    print(pet.walk())
