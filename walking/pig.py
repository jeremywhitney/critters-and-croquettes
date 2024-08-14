from datetime import date


class Pig:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()


peaches = Pig("Peaches", "Göttingen minipig", "morning")
print(
    f"{peaches.name} the {peaches.species} is available to pet during the {peaches.shift} shift."
)
