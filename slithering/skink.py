from datetime import date


class Skink:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


ziggy = Skink("Ziggy", "Common five-lined skink", "Insect Trail Mix")
print(f"{ziggy.name} is a {ziggy.species}.")
ziggy.feed()
