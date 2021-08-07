from datetime import datetime


num_list = [2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 11, 13, 14]



def my_decor(func):
    def wrapper():
        x = datetime.now()
        print("Начало выполнения")
        result = func()
        print(datetime.now() - x)
        return result

    return wrapper()


@my_decor
def my_func():
    summ = 0
    for i in range(100000):
        summ += i


print(my_func)


def my_dec(func):
    def wrapper(n):
        sp_2 = []
        for i in n:
            if i % 2 != 0:
                sp_2.append(i)
        return func(sp_2)

    return wrapper


@my_dec
def my_func1(n):
    for i in n:
        print(i)
    return n


print(my_func1(num_list))


def num1(n):
    for i in n:
        if i % 2 == 0:
            n.remove(i)
        print(num_list)


def my_dec(func2):
    def wraper(*args):
        return func2(*args[:: -1])

    return wraper


@my_dec
def func2(a, b):
    return a - b


print(func2(112, 56))
