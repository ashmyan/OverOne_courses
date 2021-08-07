from random import randint

s = []
x_ = 0
for i in range(5):
    s.append([])
    for j in range(5):
        s[i].append((randint(1, 20)))
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] > x_:
                x_ = s[i][j]

print(s)
print(x_)
