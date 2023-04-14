import random
import sys

nb = random.randint(1, 99)
attempts = 1
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("")

while True:
    try:
        guess = input("What's your guess between 1 and 99? ")
    except EOFError:
        print()
        print("Goodbye!")
        sys.exit(0) 
    if (guess == "exit"):
        print("Goodbye!")
        sys.exit(0) 
    try:
        guess = float(guess)
    except:
        print("That's not a number.")
        continue
    if (guess > nb):
        print("Too high!")
    elif (guess < nb):
        print("Too low!")
    elif (guess == nb):
        if (attempts == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
        if (nb == 42):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("You won in " + str(attempts) + " attempts!")
        sys.exit(0)
    attempts += 1
