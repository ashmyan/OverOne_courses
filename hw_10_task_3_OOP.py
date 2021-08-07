class A:
    def smthing1(self):
        print('AA')


class B(A):
    def smthing(self):
        super().smthing1()
        print('BB')


class Human:
    default_name = 'Jhon'
    default_age = 21

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 2000
        self.__house = None

    def info(self):
        return self.name, self.age, self.__house, self.__money

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def __make_deal(self, house, price):
        self.__house = house
        self.__money -= price
        print("Buy house")

    def ean_money(self, money):
        self.__money += money

    def buy_house(self, house, discont):
        if self.__money > House.final_price(discont):
            self.__make_deal(house, House.final_price(discont))
            print("Осталось ", self.__money, "$.")
        else:
            print("Недостаточно денег на счету.")


class House:
    def __init__(self, area=None, price=4000):
        self._area = area
        self._price = price

    def final_price(self, discont):
        return self._price * (discont / 100)


class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)


class Employee:

    def __init__(self, fio=None, exp=None, money_per_hour=None, amount_of_hours=None):
        self._fio = fio
        self._exp = exp
        self._money_per_hour = money_per_hour
        self._amount_of_hours = amount_of_hours

    def allcash(self):
        money = self._money_per_hour * self._amount_of_hours
        if self._exp < 1:
            pass
        elif self._exp < 3:
            money += money * 0.05
        elif self._exp < 5:
            money += money * 0.08
        else:
            money += money * 0.15
        print(money)


first_empl = Employee('Employee 1', 3, 40, 6504)
second_empl = Employee('Employee 2', 6, 50, 13453)
third_empl = Employee('Employee 3', 1, 15, 1943)
fourth_empl = Employee('Employee 4', 5, 63, 11034)
fifth_empl = Employee('Employee 5', 2, 32, 4540)

first_empl.allcash()
second_empl.allcash()
third_empl.allcash()
fourth_empl.allcash()
fifth_empl.allcash()
