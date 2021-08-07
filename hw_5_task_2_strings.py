# Замена цифры на слово
my_str = 'IamNumber1ornot1'
print(my_str.replace('1', 'one'))



# Индэкс второй буквы f
my_Fstr = 'Iam from freedom'
summ = 0
while summ < 2:
    for i, j in enumerate(my_Fstr):
        if 'f' == j:
            summ += 1
            print('-1')
            if summ == 2:
                print(i)
        elif 'f' not in my_Fstr:
            print('-2')
