evens_sum = 0

for number in range(1 , 101):
    if(number % 2 == 0){
        evens_sum += number
    }
print(f"Total summation of evens is : {evens_sum}")