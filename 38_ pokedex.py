
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types  
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        """Prints the Pokémon’s sound (usually their name twice)."""
        print(f"{self.name}! {self.name}!")

    def display_details(self):
        """Displays all the Pokémon details."""
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!\n")
        else:
            print(f"{self.name} has not been caught yet.\n")

pikachu = Pokemon(
    entry=25,
    name="Pikachu",
    types=["Electric"],
    description="It has small electric sacs on both its cheeks. "
                "If threatened, it looses electric charges from the sacs.",
    is_caught=True
)

bulbasaur = Pokemon(
    entry=1,
    name="Bulbasaur",
    types=["Grass", "Poison"],
    description="A strange seed was planted on its back at birth. "
                "The plant sprouts and grows with this Pokémon.",
    is_caught=False
)

charmander = Pokemon(
    entry=4,
    name="Charmander",
    types=["Fire"],
    description="Obviously prefers hot places. When it rains, "
                "steam is said to spout from the tip of its tail.",
    is_caught=True
)

pikachu.speak()
pikachu.display_details()

bulbasaur.speak()
bulbasaur.display_details()

charmander.speak()
charmander.display_details()
