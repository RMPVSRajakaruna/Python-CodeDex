# Write code below 💖

h = float(input('Enter your height: '))
c = int(input('Enter your credit: '))

if h >= 137 and c >= 10:
  print('Enjoy the ride!')
elif h < 137 and c >= 10:
  print('You are not tall enough to ride.')
elif h >= 137 and c < 10:
  print("You don't have enough credits.")
else:
  print('You have not met either requirement.')