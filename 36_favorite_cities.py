# Write code below 💖

class City:
    def __init__(self, name, country, population, landmarks, nickname=None, founding_year=None, mayor=None):
        self.name = name
        self.country = country
        self.population = population     
        self.landmarks = landmarks       
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor

colombo = City(
    name="Colombo",
    country="Sri Lanka",
    population=6000,  
    landmarks=["Galle Face Green", "Lotus Tower", "Old Parliament"],
    nickname="Commercial Capital",
    founding_year=1505,
    mayor="Rosy Senanayake"
)

new_york = City(
    name="New York City",
    country="USA",
    population=8450000,
    landmarks=["Statue of Liberty", "Times Square", "Central Park"],
    nickname="The Big Apple",
    founding_year=1624,
    mayor="Eric Adams"
)

print(vars(colombo))
print(vars(new_york))
