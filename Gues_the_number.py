from art import logo, project_name
import random

print(logo)
print(project_name)
print("Welcome to the Number Guessing Game !")
print("I am thinking of a number between 1 and 100.")
in_input = "Choose a difficult . Type 'easy' or 'hard':"

easy_count = 10
hard_count = 5


def number_guessing(diff_count):
    rn_num = random.randint(1, 100)
    condition = True
    while condition:
        print(f"You have {diff_count} attempts remaining to gues the number.")
        guess = int(input("Make a guess: "))
        if rn_num < guess:
            print("Too high.")
            if diff_count > 1:
                print("Guess again.")
        elif rn_num > guess:
            print("Too low.")
            if diff_count > 1:
                print("Guess again.")
        elif rn_num == guess:
            print(f"You winn")
            condition = False
        else:
            print("You have selected the wrong number.")
        diff_count -= 1
        if diff_count == 0:
            print("You've run out of guesses, you lose.")
            condition = False


ask = input(in_input)
if ask == "easy":
    number_guessing(easy_count)
else:
    number_guessing(hard_count)
