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

    def __str__(self):
        return f"{self.name} is a {self.species}."


duke = Mallard("Duke", "American pekin", "Quacker Snacks")
print(duke)
duke.feed()
