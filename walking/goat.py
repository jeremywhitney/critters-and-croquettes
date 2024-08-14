from datetime import date


class Goat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} the {self.species} is available to pet during the {self.shift} shift."


gizmo = Goat("Gizmo", "Toggenburger", "midday", "Goat Gourmet")
print(gizmo)
gizmo.feed()
