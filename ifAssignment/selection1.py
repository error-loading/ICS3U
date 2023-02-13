bearing = float(input("Enter your compass bearing: "))

direction = ""

if bearing >= 315 and bearing <= 360 or bearing >= 0 and bearing <= 45:
  direction = "North"
elif bearing >= 45 and bearing < 135:
  direction = "East"
elif bearing >= 135 and bearing <= 225:
  direction = "South"
else:
  direction = "West"

print(direction)