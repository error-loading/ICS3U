# Gurjas Dhillon
# selection5.py
# this program displays multiple currencies with their exchange rates. it asks the user to choose a currency and asks how much they want and converts it for them

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

while True:
    userCur = input("Choose a currency to buy: ").strip()
    if userCur not in curs:
        print("Something went wrong. Try again.")
    else: break
userNum = float(input("How much do you want to buy? "))
converted = round(curs[userCur] * userNum, 2)
print(f"It will cost you ${converted}.")