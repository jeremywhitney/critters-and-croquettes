from datetime import date


class MiniHorse:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()


lilsebastian = MiniHorse("Li'l Sebastian", "Miniature horse", "morning")
print(
    f"{lilsebastian.name} the {lilsebastian.species} is available to pet during the {lilsebastian.shift} shift."
)
