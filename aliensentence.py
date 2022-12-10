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


def requestInput():
    message = input("Enter message to translate")
    return message


def alienTranslator():
    print("Hello")
    message = requestInput()
    if message == "" or message == None:
        print("Bye!")
        exit()
    else:
        translated_message = alienSentence(message)
        print(translated_message.capitalize())
        requestInput()



if __name__ == '__main__':
    # sentence = input("Enter sentence to translate....")
    # my_word = alienSentence(sentence)
    # print(my_word.capitalize())
    alienTranslator()
