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

    def __str__(self):
        return f"{self.name} is a {self.species}."


freckles = Goose("Freckles", "Pomeranian goose", "Goose Grains")
print(freckles)
freckles.feed()
