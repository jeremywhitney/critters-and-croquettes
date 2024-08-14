from datetime import date


class Pig:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


peaches = Pig("Peaches", "Göttingen minipig")
print(peaches.name)
print(peaches)
