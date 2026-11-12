import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def randomize_card():
    random_card = []
    for _ in range(2):
        random_card.append(random.choice(cards))
    return random_card


def sum_scores(scores):
    return sum(scores)


def check_has_blackjack(amount):
    has_blackjack = False
    if amount == 21:
        has_blackjack = True
    return has_blackjack


def check_over_21(amount):
    is_over_21 = False
    if amount > 21:
        is_over_21 = True
    return is_over_21


def detect_ace(cards):
    return 11 in cards


def replace_1_instead_11(cards):
    while 11 in cards and sum_scores(cards) > 21:
        cards[cards.index(11)] = 1
    return cards


def add_new_card():
    return random.choice(cards)


user_cards = randomize_card()
computer_cards = randomize_card()
user_scores = 0
computer_scores = 0

should_continue = True

def user_continue_blackjack():
    while should_continue:
        user_scores = sum_scores(user_cards)
        computer_scores = sum_scores(computer_cards)

        print(user_cards, computer_cards)
        print(user_scores, computer_scores)

        user_has_blackjack = check_has_blackjack(user_scores)
        computer_has_blackjack = check_has_blackjack(computer_scores)

        if (not user_has_blackjack) and (not computer_has_blackjack):
            is_user_over_21 = check_over_21(user_scores)
            if is_user_over_21:
                user_has_ace = detect_ace(user_cards)
                if not user_has_ace:
                    print("You lose!")
                    should_continue = False
                else:
                    user_replcaced_1_instead_ace = replace_1_instead_11(user_cards)
                    user_scores = sum_scores(user_replcaced_1_instead_ace)
                    is_user_over_21 = check_over_21(user_scores)
                    if is_user_over_21:
                        print("You lose")
                        should_continue = False
            if should_continue:
                user_wants_another_card = input(
                    "Do you want another card? (type 'y' or 'n')").lower()
                if user_wants_another_card == "y":
                    user_cards.append(add_new_card())
                else:
                    should_continue = False

        elif user_has_blackjack:
            print("You won!")
            should_continue = False
        elif computer_has_blackjack:
            print("You lose!")
            should_continue = False



def computer_continue_blackjack() :
    while computer_scores < 17:
        computer_cards.append(add_new_card())
        computer_scores = sum_scores(computer_cards)


def specify_winner():
    if computer_scores > 21:
        print("You won")
    else:
        if user_scores == computer_scores:
            print("It's a draw")
        elif user_scores > computer_scores:
            print("You won!")
        else:
            print("You lose")

user_continue_blackjack()
computer_continue_blackjack()
specify_winner()


