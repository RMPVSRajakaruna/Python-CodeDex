import math

print("==================")
print("Area Calculator 📐")
print("==================")
print()
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print()

choice = int(input("Which shape: "))

if choice == 1:
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (base * height) / 2
    print("\nThe area is", area)

elif choice == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    print("\nThe area is", area)

elif choice == 3:
    side = float(input("Side: "))
    area = side * side
    print("\nThe area is", area)

elif choice == 4:
    radius = float(input("Radius: "))
    area = math.pi * radius * radius
    print("\nThe area is", area)

elif choice == 5:
    print("Goodbye!")

else:
    print("Invalid choice")
