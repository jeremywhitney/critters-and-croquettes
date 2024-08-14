from datetime import date


class Pig:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


peaches = Pig("Peaches", "Göttingen minipig", "morning", "Piggy Pantry")
print(
    f"{peaches.name} the {peaches.species} is available to pet during the {peaches.shift} shift."
)
peaches.feed()
