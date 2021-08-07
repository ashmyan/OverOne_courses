from datetime import timedelta
from datetime import datetime


def season():
    mounth = int(input("Введите номер месяца"))
    if 1 <= mounth <= 2 or mounth == 12:
        print("Winter")
    elif 3 <= mounth <= 5:
        print("Spring")
    elif 6 <= mounth <= 8:
        print("Summer")
    elif 9 <= mounth <= 11:
        print("Autumn")


season()

all_trains = [{'2, Minsk, '"2021-04-21 21:50:00": 'Moscow, '"2021-04-22 08:00:00"},
              {'16 S-Piterburg "2021-06-05 12:20:00"': 'Berlin "2021-06-06 10:00:00"'},
              {'5 Gomel "2021-05-15 07:15:00"': 'Grodno "2021-05-15 11:30:00"'}]
train = {}
fersus = timedelta(hours=7, minutes=20, seconds=0)

exit = 0
while exit != 1:
    user = int(input("Выберите категорию"))
    if user == 1:
        train[input("Введите информацию о поезде")] = input("Место и время прибытия")
        all_trains.append(train)
    elif user == 2:
        print(all_trains)
    elif user == 3:
        for i in all_trains:
            for k, v in i.items():
                d1 = (datetime.strptime(k, "%Y-%m-%d %H:%M:%S"))
                d2 = (datetime.strptime(v, "%Y-%m-%d %H:%M:%S"))
                if d2 - d1 >= fersus:
                    print(k, v)
    elif user == 4:
        exit += 1
        print("Exit")

print(all_trains)
