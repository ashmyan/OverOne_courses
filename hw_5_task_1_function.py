# Задача на парты
def school(a, b, c):
    all = (a + b + c) / 3
    return print(int(all))


school(23, 32, 21)


# Схожие числа
def numbers(a, b, c):
    if a == b == c:
        print('3')
    elif a != b and a != c and b != c:
        print('0')
    else:
        print('2')


numbers(4, 3, 3)


# Возведение в степень
def power1(a, n):
    z = 1
    for i in range(n):
        z *= a
    return z


print(power1(10, 10))
