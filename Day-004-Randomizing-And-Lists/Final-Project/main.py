import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random_index = random.randint(0, len(rock_paper_scissors) - 1)

computer_choice = rock_paper_scissors[random_index]

if (user_choice <= len(rock_paper_scissors) - 1 and user_choice >= 0):
    print(rock_paper_scissors[user_choice])


print(f"Computer chose:\n{computer_choice}")

if (user_choice == random_index):
    print("It's a draw")
elif (user_choice == 0):
    if (random_index == 1):
        print("You lose")
    else:
        print("You won")
elif (user_choice == 1):
    if (random_index == 0):
        print("You won")
    else:
        print("You lose")
elif (user_choice == 1):
    if (random_index == 0):
        print("You lose")
    else:
        print("You won")
else:
    print("You typed an invalid number, you lose!")
