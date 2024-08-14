from datetime import date


class Mallard:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


duke = Mallard("Duke", "American pekin", "Quacker Snacks")
print(f"{duke.name} is a {duke.species}.")
duke.feed()
