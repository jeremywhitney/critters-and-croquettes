from datetime import date


class Goat:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


gizmo = Goat("Gizmo", "Toggenburger")
print(gizmo.name)
print(gizmo)
