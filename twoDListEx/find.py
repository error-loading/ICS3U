def find(lst, val):
    for i in range(len(lst)):
        if val in lst[i]:
            return (i, lst[i].index(val))
    return (-1, -1)
