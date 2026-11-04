print("Welcome to python pizza delivers!")
size = input("What size of pizza do you want? S, M or L?\n")

bill = 0

add_pepperony = input("Do you want pepperony? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if(size == "S"):
    bill = 15
elif(size == "M") :
    bill = 20
else :
    bill = 25

if(add_pepperony == "Y"):
    if(size == "S"):
        bill +=2
    else :
        bill +=3

if(extra_cheese == "Y"):
    bill +=1

print(f"Your final bill is: ${bill}")