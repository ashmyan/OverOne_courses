while True:
    x = int(input("X"))
    y = int(input("Y"))
    sign = ('+', '-', '*', '/')
    s = input("Введите знак")
    if s in sign:
        if s == 0:
            break
        elif s == '+':
            z = x +y
            print(z)
        elif s == '-':
            z = x - y
            print(z)
        elif s == '*':
            z = x * y
            print(z)
        elif s == '/' and y == 0:
            print("На ноль не делят")
        elif s == '/':
            z = x / y
            print(z)


