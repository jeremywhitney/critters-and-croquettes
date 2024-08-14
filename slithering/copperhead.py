from datetime import date


class Copperhead:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


rusty = Copperhead("Rusty", "Eastern copperhead", "Snake Snax")
print(f"{rusty.name} is a {rusty.species}.")
rusty.feed()
