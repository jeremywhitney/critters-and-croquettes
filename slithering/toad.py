from datetime import date


class Toad:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()


toby = Toad("Toby", "American toad")
print(toby.name)
print(toby)
