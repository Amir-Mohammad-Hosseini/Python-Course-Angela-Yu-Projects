row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

selected_column = int(position[0])
selected_row = int(position[1])

map[selected_column-1][selected_row-1] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")