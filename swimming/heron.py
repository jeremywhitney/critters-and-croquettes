from datetime import date


class Heron:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()


sage = Heron("Sage", "Great blue heron")
print(sage.name)
print(sage)
