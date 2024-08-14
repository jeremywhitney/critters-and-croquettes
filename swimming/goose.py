from datetime import date


class Goose:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()


freckles = Goose("Freckles", "Pomeranian goose")
print(freckles.name)
print(freckles)
