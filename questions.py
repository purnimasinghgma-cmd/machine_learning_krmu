from day7 import Ques

questions = [
    "National bird of India\n(a) Peacock\n(b) Hen\n(c) Crow",

    "National animal of India\n(a) Lion\n(b) Tiger\n(c) Elephant",

    "Capital of India\n(a) Mumbai\n(b) Delhi\n(c) Kolkata",

    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter",

    "How many days are there in a week?\n(a) 5\n(b) 7\n(c) 10",

    "Which is the largest ocean in the world?\n(a) Indian Ocean\n(b) Atlantic Ocean\n(c) Pacific Ocean",

    "What is the boiling point of water?\n(a) 50°C\n(b) 100°C\n(c) 150°C",

    "Which language is used to create Python programs?\n(a) Python\n(b) HTML\n(c) CSS",

    "How many legs does a dog have?\n(a) 2\n(b) 4\n(c) 6",

    "Which is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars"
]

all_ques = [ Ques(questions[0],
 "a"), Ques(questions[1], "b"), Ques(questions[2], "c"), Ques(questions[3], "d"), Ques(questions[4], "b"), Ques(questions[5], "a"), Ques(questions[6], "c"), Ques(questions[7], "b"), Ques(questions[8], "c"), Ques(questions[9], "d"), Ques(questions[10], "a") ]
score = 0
for i in all_ques:
    answer = input( i.que)
    if answer == i.ans:
        score = score+1

print("total score:", score)


