from random import randint

n = int(input("N"))
m = int(input("M"))

matrix = []

for i in range(n):
    a_s = []
    for j in range(m):
        a_s.append(randint(1, 10))
    matrix.append(a_s)

print(matrix)
