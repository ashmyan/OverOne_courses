from random import randint

matrix_a = []
matrix_b = []
n = int(input("N"))
m = int(input("M"))
g = int(input("G"))
for i in range(n):
    matrix_a.append([])
    matrix_b.append([])
    for u in range(m):
        matrix_a[i].append(randint(1, 20))
        matrix_b[i].append(randint(1, 20))
print(matrix_a)
print(matrix_b)

sum_a = 0
sum_b = 0
sum_all = 0

for o in matrix_a:
    sum_a += sum(o)
for p in matrix_b:
    sum_b += sum(p)
sum_all = sum_a + sum_b

print(sum_a)
print(sum_b)
print(sum_all)

sum_r = 0
matrix_c = []
for y in range(n):
    matrix_c.append([])
    for e in range(m):
        sum_r = sum_all / (n * m)
        matrix_c[y].append(sum_r)

print(matrix_c)

sum_all2 = sum_a - sum_b
print(sum_all2)

sum_r2 = 0
matrix_e = []
for y in range(n):
    matrix_e.append([])
    for e in range(m):
        sum_r2 = sum_all2 / (n * m)
        matrix_e[y].append(sum_r2)

print(matrix_e)

matrix_g = []
for v in range(len(matrix_a * g)):
    matrix_g.append([])
    for d in range(m * g):
        matrix_g[v].append(randint(1, 20))

print(matrix_g)
