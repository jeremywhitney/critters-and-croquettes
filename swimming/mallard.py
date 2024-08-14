from datetime import date


class Mallard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()


duke = Mallard("Duke", "American pekin")
print(duke.name)
print(duke)
