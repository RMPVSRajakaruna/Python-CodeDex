
from math import pi
from random import choice as ch

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")
    r = 0  

if r > 0:
    area = 4 * pi * (r ** 2)

    area = round(area, 2)

    print(f"The surface area of {random_planet} is approximately {area} square kilometers.")
