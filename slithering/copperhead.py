from datetime import date


class Copperhead:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()


rusty = Copperhead("Rusty", "Eastern copperhead")
print(rusty.name)
print(rusty)
