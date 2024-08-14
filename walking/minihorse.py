from datetime import date


class MiniHorse:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


lilsebastian = MiniHorse("Li'l Sebastian", "Miniature horse", "morning", "Carrots")
print(
    f"{lilsebastian.name} the {lilsebastian.species} is available to pet during the {lilsebastian.shift} shift."
)
lilsebastian.feed()
