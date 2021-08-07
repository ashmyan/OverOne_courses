import json


with open('New_File2', 'r') as f1, open('DZ1', 'w') as f2:
    for i in f1.readlines():
        f2.write(i.replace('1', 'one'))


with open('New_File2', 'r') as f1, open('DZ1', 'r') as f2:
    f1 = f1.readlines()
    f2 = f2.readlines()
    for i in range(len(f1)):
        if f1[i] == f2[i]:
            print(i)
            break


with open('test11.json', 'w') as f:
    json.dump({'a': 1, 'b': 2}, f, indent=4)


with open('test11.json', 'r') as f:
    data = json.load(f)
    data['a'] = 10
