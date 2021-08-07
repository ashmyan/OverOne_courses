def two_numbers(a, b):
    if a != b and a != 0 and b != 0:
        if a > b:
            return two_numbers(a - b, b)
        else:
            return two_numbers(a, b - a)
    return a, b


print(two_numbers(54, 72))



def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(4))
