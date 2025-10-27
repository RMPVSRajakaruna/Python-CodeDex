# Write code below 💖

# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin


# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

# If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
# Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
# Else, output the message "Wrong input."
# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

# If the answer is 1, Hufflepuff +2.
# Else if answer is 2, Slytherin +2.
# Else if answer is 3, Ravenclaw +2.
# Else if answer is 4, Gryffindor +2.
# Else, output the message "Wrong input."
# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

# If the answer is 1, Slytherin +4.
# Else if the answer is 2, Hufflepuff +4.
# Else if the answer is 3, Ravenclaw +4.
# Else if the answer is 4, Gryffindor +4.
# Else, output "Wrong input."
# Lastly, print out the score for each house.

Gryffindor = Ravenclaw = Hufflepuff = Slytherin = 0

a = int(input('Q1) Do you like Dawn or Dusk? (1 = Dawn, 2 = Dusk) :'))
if a == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif a == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print('Wrong input!')

b = int(input('Q2) When I’m dead, I want people to remember me as: (1 = The Good, 2 = The Great, 3 = The Wise, 4 = The Bold) :'))
if b == 1:
  Hufflepuff = Hufflepuff + 2
elif b == 2:
  Slytherin = Slytherin + 2
elif b == 3:
  Ravenclaw = Ravenclaw + 2
elif b == 4:
  Gryffindor = Gryffindor + 2
else:
  print('Wrong input!')

c = int(input('Q3) Which kind of instrument most pleases your ear? (1 = The violin, 2 = The trumpet, 3 = The piano, 4 = The drum) :'))
if c == 1:
  Slytherin = Slytherin + 4
elif c == 2:
  Hufflepuff = Hufflepuff + 4
elif c == 3:
  Ravenclaw = Ravenclaw + 4
elif c == 4:
  Gryffindor = Gryffindor + 4
else:
  print('Wrong input!')

print('Gryffindor house score : ', Gryffindor)
print('Ravenclaw house score : ', Ravenclaw)
print('Hufflepuff house score : ', Hufflepuff)
print('Slytherin house score  : ', Slytherin)
 