from aliensentence import alienSentence


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
