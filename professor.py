"""
implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein 
each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct 
(or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem. If the user has 
still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
"""
import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = x + y

        for _ in range(3):
            user_input = input(problem)

            try:
                user_answer = int(user_input)
            except ValueError:
                print("EEE")
                continue

            if user_answer == answer:
                score += 1
                break
            else:
                print("EEE")

        else:
            print(f"The correct answer is {answer}")

    print("Your score:", score)

def get_level():
    while True:
        level = input("Enter a level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()
