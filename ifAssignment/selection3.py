# Gurjas Dhillon
# selection5.py

# Without ifs

fares = {
  "Adults": {
    "1": "$2.35",
    "10": "$20.30",
    "Transit Pass": "$75"
  },
  "Senior": {
    "1": "$1.60",
    "10": "$15.60",
    "Transit Pass": "$38.50"
  },
  "Student": {
    "1": "$1.60",
    "10": "$15.60",
    "Transit Pass": "$52"
  }
}

print("Welcome to Transit Windsor! (This demo is without ifs)\n")
for age in fares.keys():
  print(age)
  print('-' * len(age))
  for type in fares[age].keys():
    price = fares[age][type]
    print(f"{type}\t{price}")

  print()

while True:
  category = input("What is your age category? (Adults, Senior, or Student) ").strip()
  tickets = input("How many? (1, 10, Transit Pass) ")

  try:
    print(f"Price - {fares[category][tickets]}")
    break

  except:
    print("Something went wrong, try again.\n")

# With ifs
print("Welcome to Transit Windsor! (This demo is with ifs)\n")

category = input(
  "What is your age category? (Adults, Senior, or Student) ").strip()
tickets = input("How many? (1, 10, Transit Pass) ")

if category == "Adults":
  if tickets == "1":
    print(f"Price - {fares[category][tickets]}")

  elif tickets == "10":
    print(f"Price - {fares[category][tickets]}")
  elif tickets == "Transit Pass":
    print(f"Price - {fares[category][tickets]}")

elif category == "Senior":
  if tickets == "1":
    print(f"Price - {fares[category][tickets]}")

  elif tickets == "10":
    print(f"Price - {fares[category][tickets]}")
  elif tickets == "Transit Pass":
    print(f"Price - {fares[category][tickets]}")

elif category == "Student":
  if tickets == "1":
    print(f"Price - {fares[category][tickets]}")

  elif tickets == "10":
    print(f"Price - {fares[category][tickets]}")
  elif tickets == "Transit Pass":
    print(f"Price - {fares[category][tickets]}")
