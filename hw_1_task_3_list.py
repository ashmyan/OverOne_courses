lst = [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
for k in range(len(lst)):
    lst.sort()
    print(lst)
for i, j in enumerate(lst):
    if j % 2 == 0:
        lst[i] = lst[-1]
print(lst)
