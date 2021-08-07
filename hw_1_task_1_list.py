a = [1, 2, 3, 4, 5, 6]
b = []
step = int(input("Step"))
for i in range(step, len(a)):
    b.append(a[i])
for i in range(0, step):
        b.append(a[i])
print(b)