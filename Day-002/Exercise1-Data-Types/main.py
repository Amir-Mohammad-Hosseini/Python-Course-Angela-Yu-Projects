import random

# Data Types :

# 1. String : "Hello"
print("String "  "Hello"[0])  # -> H

# 2. Integer : 18
print("Integer ", 18 + 19)
print("Large Integer ", 378_126_900)  # Large integers

# 3. Float : 3.14
print("Float ", 3.14159)

# 4. Boolean : True or False
print("Boolean ", True)


# Type function and convert types
name_char_count = len(input("What is your name ?\n"))
converted_name_char_count = str(name_char_count)
print("Your name has " + converted_name_char_count + " characters.")

print("\n")
print(70 + float("170.5"))

print("============== Exercise ==============")

print("\n")

two_digits_number = input("Enter a 2-digits number : \n")

first_digit = int(two_digits_number[0])
second_digit = int(two_digits_number[1])

summation_digits = first_digit + second_digit

print(summation_digits)