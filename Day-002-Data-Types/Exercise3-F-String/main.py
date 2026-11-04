# F-String

score = 0
height = 1.84
isWinning = True

print(f"Your score is {score}, Your height is {height}, Your winning is {isWinning}")

print("\n")

print("============== Exercise ==============")

print("\n")

age = int(input("What is your current age ?\n"))
full_age = 90

remaining_age = full_age - age

remaining_days = remaining_age * 365
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")
