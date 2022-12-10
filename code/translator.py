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
# function to request user input
def requestInput():
    message = input("Enter message to translate \n")
    return message


# function to translate
def alienTranslator(greetings):
    print(greetings)
    message = requestInput()
    return message

# check the entered message and translate
def translate(message):
    if message == "" or message == None:
        print("Bye!")
        exit()
    else:
        translated_message = alienSentence(message)
        print(translated_message.capitalize())
        message = alienTranslator("")
        translate(message)

# main function
if __name__ == '__main__':
    message = alienTranslator("Hello!")
    translate(message)
