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


gizmo = Goat("Gizmo", "Toggenburger", "midday", "Goat Gourmet")
print(
    f"{gizmo.name} the {gizmo.species} is available to pet during the {gizmo.shift} shift."
)
gizmo.feed()
