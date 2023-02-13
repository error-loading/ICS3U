# Gurjas Dhillon
# selection5.py
# Storing the questions in a dictionary. Then access the questions using a while loop and a counter to keep track of the correct answers

from random import randint

print("Welcome to Soccer Trivia! You will be asked 10 questions and at the end, you will get a score out of 10. Good Luck")

questions = {
  1 : {
    "q" : "Who has the most ballon d'hors? ",
    "a" : ["messi"]
  }, 
  
  2 : {
    "q" : "Who won the 2022 World Cup? ",
    "a" : ["argentina"]
  }, 

  3 : {
    "q" : "Who won the first World Cup? ",
    "a" : ["uruguay"]
  }, 

  4 : {
    "q" : "Which country has the most World Cups? ",
    "a" : ["brazil"]
  }, 

  5 : {
    "q" : "Who has scored the most goals in World Cup history? ",
    "a" : ["klose"]
  }, 

  6 : {
    "q" : "What was the first World Cup trophy called? ",
    "a" : ["jules rimet trophy"]
  },

  7 : {
    "q" : "Name 1 of the hosting countries for the 2026 World Cup: ",
    "a" : ["canada", "america", "us",  "mexico", "usa", "united states of america"]
  },

  8 : {
    "q" : "In what year was the first Women's World Cup? ",
    "a" : ["1991"]
  },

  9 : {
    "q" : "How often is the world cup held? ",
    "a" : ["4"]
  },

  10 : {
    "q" : "What year did Argentina win there first World Cup? ",
    "a" : ["1978"]
  }
}

feedback = ["Close!", "Nice try!", "Nope.", "Try again!"]
questionNum = 1
ttl = 0

while questionNum <= 10:
  userAns = input(f"Question {questionNum}: {questions[questionNum]['q']}").strip().lower()
  if userAns in questions[questionNum]['a']:
    ttl +=1
    print("Good job!")
  else:
    ind = randint(0, len(feedback) - 1)
    print(f"{feedback[ind]} The correct answer was {questions[questionNum]['a'][0].title()}.")

  print()
  questionNum += 1

percentage = ttl * 10
print(f"Thank you for playing! Your score was {percentage}%")