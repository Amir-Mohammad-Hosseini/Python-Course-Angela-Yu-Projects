from art import logo
from art import vs_logo
from data import data
import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


data_length = len(data)
selected_indexes = []


def generate_random_index():
    random_data_index = random.randint(0, data_length - 1)
    while random_data_index in selected_indexes:
        random_data_index = random.randint(0, data_length - 1)
    selected_indexes.append(random_data_index)
    return random_data_index


def print_compare_data(compare_char, compare_data):
    print(
        f"Compare {compare_char}:{compare_data["name"]}, a {compare_data["description"]} from {compare_data["country"]}.")


def higher_lower_logic_fn():
    compare1_index = generate_random_index()
    score = 0
    is_game_over = False
    while not is_game_over and len(selected_indexes) < data_length:
        compare2_index = generate_random_index()
        print(logo)

        compare1_data = data[compare1_index]
        compare2_data = data[compare2_index]

        compare1_followers = compare1_data["follower_count"]
        compare2_followers = compare2_data["follower_count"]

        print_compare_data("A" ,compare1_data)
        print(vs_logo)
        print_compare_data("B" ,compare2_data)

        user_response = input(
            "Who has more followers? Type 'A' or 'B': ").lower()

        is_compare1_followers_more = compare1_followers > compare2_followers
        if is_compare1_followers_more:
            if user_response == "a":
                score += 1
                clear()
            else:
                is_game_over = True
        else:
            if user_response == "b":
                score += 1
                clear()
                compare1_index = compare2_index
            else:
                is_game_over = True
    return is_game_over, score


def show_game_result(is_game_over, score):
    if is_game_over:
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print("Congratulations! You answered all questions correctly.")


is_game_over, score = higher_lower_logic_fn()
show_game_result(is_game_over, score)
