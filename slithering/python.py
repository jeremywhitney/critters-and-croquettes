from datetime import date


class Python:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


slinky = Python("Slinky", "Ball python", "Serpent Munchables")
print(f"{slinky.name} is a {slinky.species}.")
slinky.feed()
