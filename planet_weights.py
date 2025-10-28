
earth_weight = float(input("Enter your Earth weight (in kg): "))

planet_number = int(input("Enter the planet number (1-7): "))

if planet_number == 1:
    weight = earth_weight * 0.38
    print("Your weight on Mercury is", weight, "kg")
elif planet_number == 2:
    weight = earth_weight * 0.91
    print("Your weight on Venus is", weight, "kg")
elif planet_number == 3:
    weight = earth_weight * 0.38
    print("Your weight on Mars is", weight, "kg")
elif planet_number == 4:
    weight = earth_weight * 2.53
    print("Your weight on Jupiter is", weight, "kg")
elif planet_number == 5:
    weight = earth_weight * 1.07
    print("Your weight on Saturn is", weight, "kg")
elif planet_number == 6:
    weight = earth_weight * 0.89
    print("Your weight on Uranus is", weight, "kg")
elif planet_number == 7:
    weight = earth_weight * 1.14
    print("Your weight on Neptune is", weight, "kg")
else:
    print("Invalid planet number")
