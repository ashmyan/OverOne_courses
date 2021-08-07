def recurs():
    print('Hello')
    return recurs()


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


def power2(a, n):
    if n > 0:
        return a * power2(a, n - 1)
    else:
        return 1


print(power2(2, 3))


def polindromm(a):
    if len(a) < 2:
        return True
    else:
        if a[0] == a[-1]:
            return polindromm(a[1: -1])


print(polindromm('шалаш'))
