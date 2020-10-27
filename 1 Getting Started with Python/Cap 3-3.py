

number = input("Enter number between 0.0 and 1.0:")

try:
  number = float(number)

except:
  print ("Error!")
  quit()

if number >= 0.9:
  print ("A")
elif number >= 0.8:
  print ("B")
elif number >= 0.7:
  print ("C")
elif number >= 0.6:
  print ("D")
elif number < 0.6:
  print ("F")
