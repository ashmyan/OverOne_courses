str_one = 'Hello My Name Is Sasha I Am 31'


def my_string(a):
    str_two = ''
    for i in a:
        if i == i.lower():
            str_two += i
    return str_two


print(my_string(str_one))


str_tree = 'My1Name2is3Sasha490,5i6am2318Today152may'


def my_str_red(b):
    red_str = ''
    for elem in b:
        if elem.isalpha() or elem == ' ':
            red_str += elem
        else:
            red_str += ' '

    return red_str.split()


print(my_str_red(str_tree))







