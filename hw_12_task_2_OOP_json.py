import json


class Student:
    def __init__(self, name, surname, group):
        self.__name = name
        self.__surname = surname
        self.__group = group
        self.__numbers = {'math': [4, 4, 5],
                          'programming': [5, 5, 6],
                          'geom': [4, 5, 6]}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, new_group):
        self.__group = new_group

    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, new_numbers):
        self.__numbers = new_numbers

    def lessons(self):
        lesson = input('Введите предмет.')
        number = int(input('Введите оценку.'))
        if lesson in self.__numbers:
            self.__numbers[lesson].append(number)
            return self.__numbers
        else:
            return 'Такого предмета нет.'

    def __str__(self):
        return f'Name: {self.__name}, Surname: {self.__surname}, Group: {self.__group}, Lessons: {self.__numbers}'


student1 = Student('John', 'Black', 'OverOne1')
student2 = Student('Bim', 'Oluh', 'OverOne15')
student3 = Student('Sasha', 'Bobov', 'OverOne21')
student4 = Student('Ban', 'Jun', 'OverOne45')

students = [student1, student2, student3, student4]

with open('Test111111.json', 'w') as f:
    all_lst = [{'Name': stud.name, 'Surname': stud.surname, 'Group': stud.group,
                'Lessons': stud.numbers} for stud in students]

    print(all_lst)
    json.dump(all_lst, f, indent=3)

