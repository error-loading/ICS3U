# Gurjas Dhillon
# repititionEx1.py
# This program continuosly asks the user for a password, if that password is equal to the stored password, the program outputs the number of attempts and the correct the password

# Write  a  program  that  continues  to  ask  for  a  password  until  the  right  password  is  given,  then  gives  some comment.
# Feb 21, 2023

password = "testPass!123"
attemps = 1
userAns = input("Guess what the password is! ").strip()

while userAns != password:
    userAns = input("Wrong! Try again. ").strip()
    attemps +=1

if attemps == 1: print(f"Password was {password}. It took you {attemps} try")
else: print(f"Password was {password}. It took you {attemps} trys")