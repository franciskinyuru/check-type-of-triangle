def alienSentence(word: str):
    # declare in new word
    new_word = ""
    # create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # covert the word into list
    string_array = list(word.split(" "))
    # loop through the list
    for string in string_array:
        # check if the first element is an integer
        if string[0].lower().isdigit():
            new_word = new_word + string + " "
        # check if the first element is a not vowel
        elif string[0].lower() not in vowels:
            first_letter = string[0]
            string = string[1:]
            new_word = new_word + string + first_letter.lower() + "ay "
        # if vowel do the necessary
        else:
            new_word = new_word + string + "way "
    return new_word

def threeQuestions():
    ## question 1 login ##
    # declare question one ans
    Q1answer = bool
    # reverse the word
    question1 = "Birkbeck"[::-1]
    # convert to lower case
    question1.lower()
    # get the last element after reversal
    last_element = question1[-1]
    # get the count of occurrence of the last element
    count_lastelemnt = question1.lower().count(last_element.lower())
    # define the acronym value
    acronymvalue = "BBC"
    # compare the value of count of last element with length of acronym
    if (count_lastelemnt > len(acronymvalue)):
        Q1answer = True
    else:
        Q1answer = False

    # Question 2  ##
    Q2answer = bool
    # declare difference bwtn 8 and 5
    diff = 8 - 5
    # get product of 1 and 3
    prod = 1*3

    # check the diff if smaller or equal to prod
    if (diff <= prod):
        Q2answer = True
    else:
        Q2answer = False

    # Question 3 ##
    Q3answer = bool
    # declare 2 power 3
    two_power_three = pow(2, 3)
    # declare 3 power 2
    three_power_two = pow(3, 2)
    # check the two_power_three is less than three_power_two
    if (two_power_three < three_power_two):
        Q3answer = True
    else:
        Q3answer = False


    #print(Q1answer, Q2answer, Q3answer)

    return Q1answer, Q2answer, Q3answer
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
