import string
import sys 

def text_analyzer(my_string = None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''

    if (my_string is None):
        print("What is the text to analyze?")
        my_string = input()
    if (type(my_string) is not str):
        print("Argument is not a string")
    else:
        print("The text contains " + str(len(my_string)) + " character(s):")
        lower = 0
        upper = 0
        punctuation = 0
        spaces = 0
        for i in my_string:
            if (i.islower()):
                lower += 1
            elif (i.isupper()):
                upper += 1
            elif (i in string.punctuation):
                punctuation += 1
            elif (i.isspace()):
                spaces += 1
        print("- " + str(upper) + " upper letter(s)")
        print("- " + str(lower) + " lower letter(s)")
        print("- " + str(punctuation) + " punctuation mark(s)")
        print("- " + str(spaces) + " space(s)")

if __name__ == "__main__":
    if (len(sys.argv) is not 2):
        print("Invalid number of arguments")
    else:
        text_analyzer(sys.argv[1])

    