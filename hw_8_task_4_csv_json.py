import json

# 1
with open('dz2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    count = 0
    man = None
    for i in data:
        if len(i["languages"]) > count:
            count = len(i["languages"])
            man = i
    print(man)

# 2
from datetime import datetime
from datetime import timedelta

with open('dz2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    today = datetime.strptime("01/05/2021", "%d/%m/%Y")
    age_ = timedelta(days=7665)
    all_height = 0
    personal_21 = 0

    for i in data:
        if today - datetime.strptime(i["birthday"], "%d/%m/%Y") >= timedelta(days=7665):
            all_height += i['height']
            personal_21 += 1
print(all_height / personal_21)

import csv

# with open('DZZZZZZ.csv', 'a', encoding='utf-8') as f:
# writer = csv.writer(f)
# writer.writerow(input('Name Surrname Age').split(' '))


# 3
with open('DZZZZZZ.csv', 'r', encoding='utf-8') as f, open('People.json', 'w', encoding='utf-8') as f2:
    reader = csv.reader(f)
    result = []
    dict_result = {}

    for i in reader:
        if int(i[-1]) <= 12:
            result.append({'1-12': [' '.join(i)]})
        elif 12 < int(i[-1]) <= 18:
            result.append({'13-18': [' '.join(i)]})
        elif 18 < int(i[-1]) <= 25:
            result.append({'19-25': [' '.join(i)]})
        elif 25 < int(i[-1]) <= 40:
            result.append({'26-40': [' '.join(i)]})
        else:
            result.append({'40+': [' '.join(i)]})

    for i in result:
        for k, l in i.items():
            lst = []
            if k not in dict_result:
                dict_result[k] = l
            else:
                dict_result[k] += l

    for j, k in sorted(dict_result.items()):
        json.dump({j: k}, f2, ensure_ascii=False, indent=1)
        print(j, k)

# 4


with open('4Season.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    counter = 0
    while counter <= 7:
        gradus = 0
        weather = 0
        for i in reader:
            counter += 1
            gradus += int(i[-2])
            weather += int(i[-1])
        print('Погода в Минске, средняя температура: ' + str(int(gradus / 7)),
              'а средняя скорость ветра: ' + str(int(weather / 7)))

with open('personal.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    cities = []
    for i in data:
        for j, k in i.items():
            if [j] == ['city']:
                cities.append({j: k})
