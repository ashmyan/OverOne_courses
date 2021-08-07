# Поменять местами большее значение с меньшим
s_numbers = [8, 5, 12, 54, 23, 76, 121, 2, 322, 543, 1121, 2321, 34, 343, 12113, 43222, 432]
max_num = 0
min_num = s_numbers[0]
for j, i in enumerate(s_numbers):
    if i > max_num:
        max_num = i
        k = j
    elif min_num > i:
        min_num = i
        l = j
s_numbers[k], s_numbers[l] = s_numbers[l], s_numbers[k]
print(s_numbers)
print(max_num)
print(min_num)



# Переставить соседние элементы
for z, x in enumerate(s_numbers):
    if z % 2 != 0:
        s_numbers[z], s_numbers[z - 1] = s_numbers[z - 1], s_numbers[z]

print(s_numbers)
