# Gurjas Dhillon
# selection5.py

curs = { 
  "US" : 0.74807,
  "Euro" : 0.69943,
  "Pound" : 0.61750,
  "Yen" : 97.788,
  "Franc" : 0.69081
}
curNum = 1
print("Welcome to Xe.com")

for keys in curs.keys():
    print(f"{curNum}.\t{keys}\t{curs[keys]}")
    curNum +=1

userCur = input("Choose a currency to buy: ").strip()
userNum = float(input("How much do you want to buy? "))
converted = round(curs[userCur] * userNum, 2)
print(f"It will cost you ${converted}.")