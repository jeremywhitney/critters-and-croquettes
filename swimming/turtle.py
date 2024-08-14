from datetime import date


class Turtle:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


turbo = Turtle("Turbo", "Painted turtle", "Pizza")
print(f"{turbo.name} is a {turbo.species}.")
turbo.feed()
