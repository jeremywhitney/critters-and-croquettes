from datetime import date


class Skink:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()


ziggy = Skink("Ziggy", "Common five-lined skink")
print(ziggy.name)
print(ziggy)
