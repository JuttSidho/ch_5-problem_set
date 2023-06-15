"""
implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random
random = random.randint (1, 50)
# print(random)
userGues = None
guess = 0
while (userGues != random):

    userGues = int(input('Enter your guess: '))
    guess += 1

    if (userGues==random):
        print("your guess is right")
    else :
        if (userGues>random):
            print('you guess it wrong! enter smalar number')
        else :
            print('you guess it wrong! enter a larger number')

print(f"yours guessed tne num in {guess} guesses")
