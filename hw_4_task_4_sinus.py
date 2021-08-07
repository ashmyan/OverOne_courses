def factorial(n):
    mul = 1
    for i in range(1, n + 1):
        mul *= i
    return mul


print(factorial(5))


def sin1(x, e):
    result = 0
    n = 1
    temp = x
    while abs(temp) > e:
        result += temp
        temp = pow(-1, n) * (pow(x, ((2 * n + 1) / factorial(2 * n + 1))))
        n += 1
    return result


print(sin1(5, 2))
