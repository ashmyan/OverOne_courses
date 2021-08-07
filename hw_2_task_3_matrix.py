from random import randint

summ = 0
summ2 = 0
n = int(input("N"))
m = int(input("M"))
s = []

for i in range(n):
    s.append([])
    for j in range(m):
        s[i].append(randint(1, 10))
for i in range(n):
    for j in range(m):
        if s[i][j] > (n + m) / 2:
            summ += 1
for i in range(n):
    for j in range(m):
        if s[i][j] % 2 == 0:
            summ2 += s[i][j]

print(summ2)
