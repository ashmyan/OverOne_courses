from random import randint
a = []
n = int(input("N"))
for i in range(n):
    a.append(randint(0, 100))
for j in range(len(a)):
    if a[j] % 2 == 0:
        a[j] /= 4
    else:
        a[j] *= 2

print(a)


b = ["яблоко", "киви", "арбуз", "банан"]
for i, elem in enumerate(b):
    print(f'{i+1}.{" "*(10-len(elem))}{elem}')

a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 2, 3, 3, 5, 5, 6, 9, 11, 12, 13, 14]
for i, elem in enumerate(a):
    if elem in b:
        del a[i]
        print(a)

any_str = "a73ab51rg89ck7"
a = []
b_str = ""
for i in range(len(any_str)):
    if any_str[i].isdigit():
        b_str += any_str[i]
    else:
        if b_str != "":
            a.append(int(b_str))
            b_str = ""
        if b_str != "":
            a.append(int(b_str))
print(a)



c = {}
for elem in b:
    if elem in c:
        c[elem] += 1
    else:
        c[elem] = 1
print(c)

