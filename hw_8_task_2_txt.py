#1
with open('DZ1.txt', 'w') as f:
    n = int(input('N'))
    for i in range(n):
        f.write(input('Введите строку') + '\n')
my_file = open('DZ1.txt')
my_file.close()

#2
with open('DZ1.txt', 'a+') as f1:
    for i in range(n):
        print(input("Строка"), file=f1)

#2
with open('DZ1.txt', 'a+') as f2:
    for line in range(3):
        f2.write(input("Еще") + '\n')

