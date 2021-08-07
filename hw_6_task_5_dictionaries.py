my_list = ['Ivanov paper 7', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7',
           'Petrov envelope 5', 'Suvorov marker 1', 'Suvorov pens 3']


def sort(lst):
    result = {}
    for elem in lst:
        new_lst = elem.split(' ')
        if new_lst[0] not in result:
            result[new_lst[0]] = None
        for key in result:
            key_result = {}
            for i in lst:
                elem = i.split(' ')
                if elem[0] == key and elem[1] not in key_result:
                    key_result[elem[1]] = int(elem[2])
                elif elem[0] == key and elem[1] in key_result:
                    key_result[elem[1]] += int(elem[2])
        key_list = [f'{k}{v}' for k, v in key_result.items()]
        key_list = sorted(key_list)
        result[key] = ' '.join(key_list)
    return result


print(sort(my_list))
