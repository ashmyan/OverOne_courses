from random import randint

n = int(input("N"))
m = int(input("M"))

matrix = []

for i in range(n):  # создане матрицы
    a_s = []
    for j in range(m):
        a_s.append(randint(1, 10))
    matrix.append(a_s)

max_el = 0

for e in matrix:  # максимальное число
    for a in e:
        if a > max_el:
            max_el = a

min_el = max_el

for e in matrix:  # минимальное число
    for a in e:
        if min_el > a:
            min_el = a

sum_matrix = 0

for e in matrix:  # сумма всех чисел
    for i in e:
        sum_matrix += i

smm = 0
for el, er in enumerate(matrix):  # строчка с наибольшей суммой и индэкс
    if sum(er) > smm:
        smm = sum(er)
        print(smm, el)

as_a = 0
for el, er in enumerate(matrix):
    if sum(er) > as_a:
        as_a = sum(er)
        if sum(er) < as_a:
            as_a = sum(er)
print(as_a)

print(matrix)
print(max_el)
print(min_el)
print(sum_matrix)
