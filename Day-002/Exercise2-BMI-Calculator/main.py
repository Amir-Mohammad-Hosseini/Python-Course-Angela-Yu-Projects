weight = float(input("Enter your weight (kilogram) :\n"))
height = float(input("Enter your height (meter) :\n"))

bmi = weight / (height ** 2)
print(round(bmi , 2))