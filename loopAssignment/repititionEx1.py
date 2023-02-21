# Write  a  program  that  continues  to  ask  for  a  password  until  the  right  password  is  given,  then  gives  some comment.
# Feb 19, 2023

password = "testPass!123"
attemps = 1
userAns = input("Guess what the password is! ").strip()

while userAns != password:
    userAns = input("Wrong! Try again. ").strip()
    attemps +=1

print(f"Password was {password}. It took you {attemps} try/trys")