# 1. Output every item from list with positive indexing.
list1 = [2, 51, 11, 13, 51, 100]
#       -6     -5    -4    -3 -2     -1
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
# 2. Output every item from list with negative indexing.
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
print(list1[-6])
# 3. Replace the last element of a list with a new value.
list1[5]=200
print(list1)
# 4. Replace the fifth element of a list with a new value.
list1[4]=60
print(list1)
# 5. Extract (ამოწერას ნიშნავს, slicing უნდა გამოიყენოთ) the last three elements of a list.
print(list1[3:6])
# 6. Extract the first three elements of a list.
print(list1[0:3])
# 7. Extract the middle two elements of a list. ([11, 13])
print(list1[2:4])
# 8. Extract random elements of a list with negative indexes.
print(list1[-5])