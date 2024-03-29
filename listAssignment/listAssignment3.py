# Gurjas Dhillon
# listAssignment3.py
# Trivia program to test the knowledge of prime ministers of the user

from random import shuffle

# ministers dictionary with all the info needed
mininisters = {
    1 : {
        'name' : "macdonald",
        'office' : '1867-1873'
    }, 
    2 : {
        'name' : "mackenzie",
        'office' : '1873-1878'
    }, 
    3 : {
        'name' : "macdonald",
        'office' : '1878-1891'
    }, 
    4 : {
        'name' : "abbott",
        'office' : '1891-1892'
    }, 
    5 : {
        'name' : "thompson",
        'office' : '1892-1894'
    }, 
    6 : {
        'name' : "bowell",
        'office' : '1894-1896'
    }, 
    7 : {
        'name' : "tupper",
        'office' : '1896-1896'
    },
    8 : {
        'name' : "laurier",
        'office' : '1896-1911'
    },
    9 : {
        'name' : "borden",

        'office' : '1911-1917'
    }, 
    10 : {
        'name' : "borden",
        'office' : '1917-1920'
    }, 
    11 : {
        'name' : "meighen",
        'office' : '1920-1921'
    }, 
    12 : {
        'name' : "king",
        'office' : '1921-1926'
    }, 
    13 : {
        'name' : "meighen",
        'office' : '1926-1926'
    }, 
    14 : {
        'name' : "king",
        'office' : '1926-1930'
    }, 
    15 : {
        'name' : "bennett",
        'office' : '1930-1935'
    }, 
    16 : {
        'name' : "king",
        'office' : '1921-1926'
    }, 
    17 : {
        'name' : "laurent",
        'office' : '1948-1957'
    }, 
    18 : {
        'name' : "diefenbaker",
        'office' : '1957-1963'
    }, 
    19 : {
        'name' : "pearson",
        'office' : '1963-1968'
    }, 
    20 : {
        'name' : "trudeau",
        'office' : '1968-1979'
    }, 
    21 : {
        'name' : "clark",
        'office' : '1979-1980'
    }, 
    22 : {
        'name' : "trudeau",
        'office' : '1980-1984'
    }, 
    23 : {
        'name' : "turner",
        'office' : '1984-1984'
    }, 
    24 : {
        'name' : "mulroney",
        'office' : '1984-1993'
    }, 
    25 : {
        'name' : "campbell",
        'office' : '1993-1993'
    }, 
    26 : {
        'name' : "chrétien",
        'office' : '1993-2003'
    }, 
    27 : {
        'name' : "martin",
        'office' : '2003-2006'
    }, 
    28 : {
        'name' : "harper",
        'office' : '2006-2015'
    }, 
    29 : {
        'name' : "trudeau",
        'office' : '2015-present'
    }, 


}

# get a list of integers from 1-29 and then shuffle them to get random indices for the trivia
nums = list(range(1, 30))
shuffle(nums)

print("Welcome to 'Another Trivia'!")

cor = 0

for i in range(10):
    ind = nums[i]     # get the index of the questions
    print(f"Question {i + 1}")
    print(f"Term Number. {ind}")
    print(f"Date {mininisters[ind]['office']}")
    user = input("What is the name of this prime minister? ").lower()     

    # if the users ans is correct, increment correct and output a msg, otherwise tell the user they are wrong and also output the right ans
    if user == mininisters[ind]['name']:
        cor += 1
        print("You are correct!")
    else:
        print(f"The answer was {mininisters[ind]['name'].title()}. Better luck next time!")

avg = cor * 10     # calculating the avg

# checking the ranges of the avg and outputting the appropriate msg
if avg < 50:
    print(f"Go back to history class. Average - {avg}%")
elif avg < 60:
    print(f"Close one! Average - {avg}%")
elif avg < 70:
    print(f"Decent score. Average - {avg}%")
else:
    print(f"Good job! Average - {avg}%")
