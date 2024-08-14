from datetime import date


class Donkey:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()


eddie = Donkey("Eddie", "Irish donkey", "midday")
print(
    f"{eddie.name} the {eddie.species} is available to pet during the {eddie.shift} shift."
)
