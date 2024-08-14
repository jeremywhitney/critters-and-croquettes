from datetime import date


class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()


sunny = Goldfish("Sunny", "Comet")
print(sunny.name)
print(sunny)
