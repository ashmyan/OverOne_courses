a = [1, 2, 3, 5, 6, 1]


def un(f):
    return len(a) == len(set(a))


print(un(a))

sp_str = ['a', 'strr', 'helloooo', 'fdf', 'ds']


def all_ea(lst):
    max_len = 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
    for i, elem in enumerate(lst):
        if len(elem) < max_len:
            lst[i] = elem + (' ' * (max_len - len(elem)))

    return lst


print(all_ea(sp_str))
