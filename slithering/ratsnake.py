from datetime import date


class RatSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()


ratatouille = RatSnake("Ratatouille", "Eastern rat snake")
print(ratatouille.name)
print(ratatouille)
