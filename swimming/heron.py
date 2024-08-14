from datetime import date


class Heron:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


sage = Heron("Sage", "Great blue heron", "Sashimi")
print(f"{sage.name} is a {sage.species}.")
sage.feed()
