from datetime import date


class Llama:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


miss_fuzz = Llama("Miss Fuzz", "Domestic llama", "afternoon", "Llama Chow")
print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)
miss_fuzz.feed()
