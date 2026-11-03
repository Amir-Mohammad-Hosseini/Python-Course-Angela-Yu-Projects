print("Welcome to the trip calculator.")
total_bill = float(input("Wat was the total bill? $"))
percentage_tip = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
people_count = int(input("how many people to split the bill? "))

total_tip = percentage_tip * total_bill / 100

each_person_pay = (total_bill + total_tip) / people_count

# two_rounded_each_person_pay = round(each_person_pay, 2)
two_rounded_each_person_pay = "{:.2f}".format(each_person_pay) # Another way for rounding floats
print(f"Each person should pay: ${two_rounded_each_person_pay}")
