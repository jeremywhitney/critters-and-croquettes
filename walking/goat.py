from datetime import date


class Goat:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()


gizmo = Goat("Gizmo", "Toggenburger", "midday")
print(
    f"{gizmo.name} the {gizmo.species} is available to pet during the {gizmo.shift} shift."
)
