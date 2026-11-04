print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_names = name1 + name2

true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count(
    "e") 

love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

str_count_true_love = str(true_count) + str(love_count)

int_count_true_love = int(str_count_true_love)

if (int_count_true_love < 10 or int_count_true_love > 90):
    print(
        f"Your score is {int_count_true_love}, you go together like coke and mentos.")
elif (int_count_true_love >= 40 and int_count_true_love <= 50):
    print(f"Your score is {int_count_true_love}, you are alright together.")
else:
    print(f"Your score is {int_count_true_love}.")
