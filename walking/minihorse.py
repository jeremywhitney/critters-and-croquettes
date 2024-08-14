from datetime import date


class MiniHorse:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


lilsebastian = MiniHorse("Li'l Sebastian", "Miniature horse")
print(lilsebastian.name)
print(lilsebastian)
