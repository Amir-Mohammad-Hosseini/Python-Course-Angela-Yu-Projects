# from replit import clear
from art import logo

print(logo)

auction_people = []
max_bid = 0
max_bid_person = ""


def find_highest_bidder(person):
    global max_bid, max_bid_person
    for key in person:
        bid = person[key]
        if bid > max_bid:
            max_bid = bid
            max_bid_person = key


should_continue = True

while should_continue:
    user_name = input("What is your name?\n")
    bid_price = int(input("How much is your bid price? \n$"))

    auction_person = {
        user_name: bid_price
    }

    auction_people.append(auction_person)

    is_another_person = input(
        'Is there another person? ("Yes" or "No")\n').lower()

    if is_another_person == "no":
        should_continue = False


for person in auction_people:
    find_highest_bidder(person)


print(f"The winner is {max_bid_person} with a bid of ${max_bid}")
