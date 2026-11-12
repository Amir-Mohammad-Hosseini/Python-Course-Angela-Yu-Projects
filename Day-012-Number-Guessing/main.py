import random
from art import winner_logo , game_over_logo

def greeting():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def create_random_number ():
    return random.randint(1 , 100)

def determine_attempts ():
    attempts = 10
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if game_difficulty == "hard":
        attempts = 5

    return attempts


def check_guessed_number (attempts):
    is_guess_true = False
    while attempts > 0 and (not is_guess_true):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Guess a number: "))

        if guess_number == random_number:
            is_guess_true = True
        else :
            if guess_number < random_number :
                print("Too low!")
            else : 
                print("Too high!")
        attempts -=1
    return is_guess_true

def show_game_result(is_guess_true):
    if is_guess_true :
        winner_logo()
    else :
        game_over_logo()


greeting()
random_number = create_random_number()
attempts = determine_attempts()
is_guess_true = check_guessed_number(attempts)
show_game_result(is_guess_true)
