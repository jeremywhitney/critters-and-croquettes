from datetime import date


class Goose:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


freckles = Goose("Freckles", "Pomeranian goose", "Goose Grains")
print(f"{freckles.name} is a {freckles.species}.")
freckles.feed()
