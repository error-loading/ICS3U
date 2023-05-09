'''
Gurjas Dhillon
funcAssign2.py
function returns all the elements that is one list but not the other
'''

def subtract(list1, list2):
    neither = [i for i in list1 if i not in list2]
    return neither

print(subtract([1, 2, 3], [2, 3, 4]))