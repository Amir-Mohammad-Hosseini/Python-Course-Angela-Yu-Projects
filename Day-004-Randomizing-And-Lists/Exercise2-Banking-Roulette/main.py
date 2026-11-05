import random
names_string = input("Give meeverybody's names, seperated by acomma. ")
names = names_string.split(", ")

# random_index = random.randint(0 , len(names) - 1)

# selected_random_name = names[random_index]

# Another way : 

selected_random_name = random.choice(names)

print(f"{selected_random_name} is going to buy the meal today.")