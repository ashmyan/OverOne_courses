from datetime import datetime
from datetime import timedelta

table = []
while True:
    print("Введите категорию")
    choice = int(input(""))
    if choice == 1:
        info = {'Number': input('Number'), 'Arival point': input('Arival point'),
                'Arival time': datetime.strptime(input('время d/m/y h:m'), '%d/%m/%Y %H:%M'),
                'Destanation': input('Destanation'),
                'Destanation time': datetime.strptime(input("время d/m/y h:m"), '%d/%m/%Y %H:%M')}
        info['Time in trip'] = info['Destanation time'] - info['Arival time']
        table.append(info)
    elif choice == 2:
        for i in table:
            print(i)
    elif choice == 3:
        for i in table:
            if i['Time in trip'] >= timedelta(hours=7, minutes=20):
                print(i)
