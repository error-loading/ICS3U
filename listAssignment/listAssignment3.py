from random import shuffle
mininisters = {
    1 : {
        'name' : "laurier",
        'term' : 7,
        'office' : '1896-1911'
    }, 
    2 : {
        'name' : "bennett",
        'term' : 11,
        'office' : '1930-1935'
    }, 
    3 : {
        'name' : "diefenbaker",
        'term' : 13,
        'office' : '1957-1963'
    }, 
    4 : {
        'name' : "turner",
        'term' : 17,
        'office' : '1984-1984'
    }, 
    5 : {
        'name' : "campbell",
        'term' : 19,
        'office' : '1993-1993'
    }, 
    6 : {
        'name' : "harper",
        'term' : 22,
        'office' : '2006-2015'
    }, 
    7 : {
        'name' : "pearson",
        'term' : 14,
        'office' : '1963-1968'
    }, 
    8 : {
        'name' : "meighen",
        'term' : 9,
        'office' : '1920-1921'
    }, 
    9 : {
        'name' : "borden",
        'term' : 8,
        'office' : '1911-1920'
    }, 
    10 : {
        'name' : "tupper",
        'term' : 6,
        'office' : '1896-1896'
    }
}

nums = list(range(1, 11))
shuffle(nums)

print("Welcome to 'Another Trivia'!")

cor = 0

for i in range(10):
    ind = nums[i]
    print(f"Question {i + 1}")
    print(f"No. {mininisters[ind]['term']}")
    print(f"Date {mininisters[ind]['office']}")
    user = input("What is the name of this prime minister? ").lower()
    if user == mininisters[ind]['name']:
        cor += 1
        print("You are correct!")
    else:
        print("Better luck next time!")

avg = cor * 10
print(f"Average - {avg}%")
