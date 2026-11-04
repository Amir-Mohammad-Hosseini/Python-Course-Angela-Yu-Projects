weight = float(input("Enter your weight (kilogram) :\n"))
height = float(input("Enter your height (meter) :\n"))

bmi = weight / (height ** 2)
rounded_bmi = round(bmi, 2)

bmi_status = ""

if (rounded_bmi < 18.5):
    bmi_status = "you are underweight"
elif (rounded_bmi >= 18.5 and rounded_bmi < 25):
    bmi_status = "you have a normal weight"
elif (rounded_bmi >= 25 and rounded_bmi < 30):
    bmi_status = "you are overweight"
elif (rounded_bmi >= 30 and rounded_bmi < 35):
    bmi_status = "you are obese"
else:
    bmi_status = "you are clinically obese."

print(f"Your bmi is {rounded_bmi}, {bmi_status}")
