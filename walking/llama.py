from datetime import date


class Llama:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


miss_fuzz = Llama("Miss Fuzz", "Domestic llama")
print(miss_fuzz.name)
print(miss_fuzz)
