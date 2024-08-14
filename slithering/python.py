from datetime import date


class Python:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()


slinky = Python("Slinky", "Ball python")
print(slinky.name)
print(slinky)
