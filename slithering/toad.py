from datetime import date


class Toad:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


toby = Toad("Toby", "American toad", "Slug Stew")
print(f"{toby.name} is a {toby.species}.")
toby.feed()
