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


ans = threeQuestions()
print(ans)
