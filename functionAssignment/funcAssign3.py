'''
Gurjas Dhillon
funcAssign3.py
create a justify function
'''

def justify(list1, sz):
    n = len(list1)

    # base cases, if the field size is too small, or nothing was inputed
    if 2*n - 1 > sz or list1 == [] or len(list1) == 1:
        return " ".join(list1)
    
    # code to get number of chars in the list
    char = 0

    for word in list1:
        char += len(word)
    
    # avg spaces between letters
    avg = (sz - char) // (len(list1) - 1)

    # how many remaining spaces are left over
    rem = sz - char - avg * (len(list1) - 1)

    sent = ""

    for i in range(len(list1)):
        # add the word
        sent += list1[i]

        # add the avg spaces as long as it's not the last word
        if i != n - 1:
            sent += " " * avg

        # add one space at the end if remaining is greater than zero
        if rem > 0:
            sent += " "
            rem -= 1
    

    return sent

print("|", justify(["all", "too", "easy"], 15), "|")