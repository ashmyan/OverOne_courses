import json

# 1
with open('DZ1.txt', 'r') as f1, open('DZ1_2.txt', 'w') as f2, open('DZ1_3.txt', 'w') as f3:
    f1 = f1.readlines()
    for i in range(len(f1)):
        if i % 2 == 0 and i != 0:
            f2.write(f1[i])
        else:
            f3.write(f1[i])



# 2
with open('DZ1_4.txt', 'r') as f4:
    f4 = f4.readlines()
    for i in f4:
        i_str = i.split(' ')
        new_str = i.split()
        new_str2 = ''.join(new_str)
        print(i, '-Слов в строке:', len(i_str), 'Букв в строке:', len(new_str2))

# 3
with open('DZ1_5.txt', 'r', encoding='utf-8') as f5:
    f5 = f5.readlines()
    summ_all = 0
    for s in f5:
        for elem in s:
            if elem.isdigit():
                summ_all += int(elem)
print(summ_all / (len(f5)))



with open('DZ1_5.txt', 'r', encoding='utf-8') as f15:
    f15 = f15.readlines()
    summ_all2 = 0
    for s in f15:
        list_ozenok = s.split()
        summ_all2 += int(list_ozenok[1])
print(round(summ_all2 / len(f15), 2))



# 4
with open('DZ1_5.txt', 'r', encoding='utf-8') as f6, open('DZ1_5_2.json', 'w', encoding='utf-8') as f7:
    f6 = f6.readlines()
    for i in f6:
        list_strok = i.split()
        json.dump({list_strok[0]: list_strok[1]}, f7, ensure_ascii=False, indent=4)

with open('DZ1_5.txt', 'r', encoding='utf-8') as f6, open('DZ1_5_2.json', 'w', encoding='utf-8') as f7:
    f6 = f6.readlines()
    lst = []
    for string in f6:
        temp_dict = {}
        string = string.split(' ')
        temp_dict['name']
