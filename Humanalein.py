import threequestion
from threequestion import threeQuestions
from aliensentence import alienSentence


def humanOtAlien():
    # question 1
    q1 = "Is the 3-time repetition pf the last character of the " \
         "reversed string of 'Birkbeck' not greater than acronym (abbreviation) of the British Broadcasting " \
         "corporation? "
    # question 2
    q2 = "Is the defference between 8 and 5 not smaller than or equal to the product of 1 and 3?"
    # question 3
    q3 = "Is 2 raised to the power of 3 less than 3 raised to the power of 2?"
    # answer for question 1
    ansq1 = input("What is your answer to Q1 \n")
    # answer for question 2
    ansq2 = input("What is your answer to Q2 \n")
    # answer for question 3
    ansq3 = input("What is your answer to Q3 \n")
    # convert answers to bool
    if ansq1.lower() == "true":
        ans1 = True
    else:
        ans1 = False

    if ansq2.lower() == "true":
        ans2 = True
    else:
        ans2 = False

    if ansq3.lower() == "true":
        ans3 = True
    else:
        ans3 = False
    # get the ans for previous solution
    three_ans = threeQuestions()
    # get collect answers count
    ans_count = 0
    # compare answers
    if three_ans[0] == ans1:
        ans_count = ans_count + 1
    if three_ans[1] == ans2:
        ans_count = ans_count + 1
    if three_ans[2] == ans3:
        ans_count = ans_count + 1
    # check number of questions answered correct
    if ans_count >= 2:
        print("You are a human")
    else:
        message = "You are an alien"
        alien_message = alienSentence(message)
        print(alien_message.capitalize())


humanOtAlien()
