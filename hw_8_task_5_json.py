import json

with open('personal.json') as f1:
    data = json.load(f1)
    summ = 0
    for i in data:
        if i['salary'] > 2000:
            print(i)
    for i in data:
        if i["city"] == "Minsk":
            summ += 1
print(summ)

with open('personal.json') as f2, open('personal2.json', 'w') as f3:
    data = json.load(f2)
    result = []
    cities = []
    for i in data:
        cities.append(i['city'])
    for i in set(cities):
        result.append({'city': i, 'personal': []})
    for i in data:
        for j in data:
            if i['city'] == j['city']:
                i['personal'].append(j['name'])





with open('stud (2).json', 'r') as f1, open('rooms1 (2).json', 'r') as f2, open('dzOMG.json', 'w') as f3:
    data1 = json.load(f1)
    data2 = json.load(f2)

    final_lst = []

    for i in data2:
        final_lst.append(i)

    for j in final_lst:
        j['students'] = []
    for i in data1:
        for j in final_lst:
            if i['room'] == j['id']:
                j['students'].append({'id': i['id'], 'name': i['name']})

    json.dump(final_lst, f3, indent=4)
