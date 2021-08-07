from random import randint


num_list = [2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 11, 13, 14]

num_list2 = [i for i in num_list if i % 2 != 0]
print(num_list2)


list_spring = ["Hello", "My", "Name", "Freeman"]

new_list = [f'{i + 1} - {e}' for i, e in enumerate(list_spring)]
print(new_list)



c = ['hello', 'good', 'morning']
d = [i for i in reversed(c)]
e = [i[:: -1] for i in c]
print(d)
print(e)



sa = [{'mark': 'Audi', 'year': 2014},
      {'mark': 'BMW', 'year': 2019}]
da = [i for i in sa for j, k in i.items() if i['year'] > 2015]
print(da)



mx = [[randint(1, 9) for j in range(3)] for i in range(3)]
print(mx)


di = {'a': 1, 'bb': 2}
dc = {k: j * 2 for j, k in di.items()}
print(dc)
