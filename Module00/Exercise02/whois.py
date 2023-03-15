import sys

if (len(sys.argv) != 2):
    print("Invalid number of arguments")
    quit()
try:
    nb = int(sys.argv[1])
except:
    print("Argument is not an integer")
    quit()

if ((nb % 2) == 0):
    print("I'm even.")

else:
    print("I'm odd.")
