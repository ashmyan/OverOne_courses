mirror = ["кот", "кок", "шалаш", "парад", "сос"]
mirror2 = []

for i in mirror:
    if i == i[:: -1]:
        mirror2.append(i)

print(mirror2)




def my_mirror(n):
    if n == n[:: -1]:
        print(n)

my_mirror("шалаш")
