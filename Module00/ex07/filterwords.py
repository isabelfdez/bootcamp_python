import sys
import string

def nopunc(word):
    for i in string.punctuation:
        word = word.replace(i, "")
    return (word)

if (len(sys.argv) != 3):
    print("Incorrect number of arguments")
    quit()

try:
    str(sys.argv[1])
    int(sys.argv[2])
except:
    print("Invalid arguments")
    quit()

txt = sys.argv[1].split()
words = [nopunc(word) for word in txt if len(nopunc(word)) > int(sys.argv[2])]
print(words)
