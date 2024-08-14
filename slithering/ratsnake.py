from datetime import date


class RatSnake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


ratatouille = RatSnake("Ratatouille", "Eastern rat snake", "RATatouille")
print(f"{ratatouille.name} is a {ratatouille.species}.")
ratatouille.feed()
