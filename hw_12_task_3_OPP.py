class Human:

    def __init__(self, name, age, profession, salary, time):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__salary = salary
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, new_profession):
        self.__profession = new_profession

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_time):
        self.__time = new_time

    def change_profession(self):
        if self.__salary <= 1500:
            return 'You need change profession'
        else:
            return 'You can do better!'

    def where_you(self):
        if 9 < self.__time < 21:
            return self.__name + ' working.'
        else:
            return self.__name + ' at home and relaxing.'


man = Human('John', 25, 'mechanic', 1400, 9.1)

print(man.name)
print(man.age)
print(man.profession)
print(man.salary)
print(man.time)
print(man.change_profession())
print(man.where_you())

man.salary = 1600
man.time = 22
print(man.change_profession())
print(man.where_you())
