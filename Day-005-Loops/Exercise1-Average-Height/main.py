student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
items_count = 0
for height in student_heights :
    sum += height 
    items_count +=1

average_height = round(sum / items_count , 2)
print(average_height)
