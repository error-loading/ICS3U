# In order for a password to be considered valid it must be at least 6 characters long and have at least one number in it and at least 1 character in it. Write a program that lets the user continue to enter possible passwords until thet enter "end". For each password tell them if it if "VALID" or "INVALID".

nums = '0123456789'
chara = '!@#$%^&*()/\:;'

def check(pw):
    if len(pw) < 6: return False
    num = False
    for i in nums:
        if i in pw: 
            num = True
            break
    
    if not num: return False

    char = False

    for i in chara:
        if i in pw:
            return True
    
    return False

password = input("Enter a password: ").strip()

while password != 'end':
    if check(password):
        print("Valid")
    else:
        print("Invalid")
    password = input("Enter a password: ").strip()
