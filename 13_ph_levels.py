# Write code below 💖

ph = float(input('Enter the PH value: '))

if ph >= 0 and ph <= 14:
  if ph > 7:
    print('Basic')
  elif ph < 7:
    print('Acidic')
  else:
    print('Neutral')
else:
  print('Enter valid value!')