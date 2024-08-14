from datetime import date


class Goldfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


sunny = Goldfish("Sunny", "Comet goldfish", "Fancy Fish Fish Pellets")
print(f"{sunny.name} is a {sunny.species}.")
sunny.feed()
