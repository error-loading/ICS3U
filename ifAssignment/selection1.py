# Gurjas Dhillon
# selection1.py
# You enter a bearing and the program outputs the direction

bearing = float(input("Enter your compass bearing: "))

direction = ""    # innitially set to empty string, then goes into conditions and assigns it a direction according to bearing

if bearing >= 315 and bearing <= 360 or bearing >= 0 and bearing <= 45:
  direction = "North"
elif bearing > 45 and bearing < 135:
  direction = "East"
elif bearing >= 135 and bearing <= 225:
  direction = "South"
else:
  direction = "West"

print(direction)