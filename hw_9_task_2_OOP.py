class Car:
    def __init__(self, mark, model, year, engine=None, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__engine = input('Start engine Yes/No?')

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    @property
    def engine(self):
        return self.__engine

    def up_speed(self):
        if self.__engine == 'Yes':
            self.__speed += 10
            print(str(self.__speed) + ' km/h')
        else:
            self.__engine = None

    def increase_speed(self):
        if self.__speed >= 10:
            self.__speed -= 10
            print(str(self.__speed) + ' km/h')
        else:
            self.__speed = 0
            print(str(self.__speed) + ' km/h')

    def stop_car(self):
        self.__speed = 0
        self.__engine = input('STOP engine Yes/No?')
        print(str(self.__speed) + ' km/h')

    def start_engine(self):
        self.__engine = input('Start engine Yes/No?')

    def check_speed(self):
        if self.__speed == 0:
            print(self.__speed, ' N')
        elif 0 < self.__speed <= 15:
            print(self.__speed, ' 1 step')
        elif 15 < self.__speed <= 30:
            print(self.__speed, ' 2 step')
        elif 30 < self.__speed <= 45:
            print(self.__speed, ' 3 step')
        elif 45 < self.__speed <= 70:
            print(self.__speed, ' 4 step')
        elif self.__speed > 70:
            print(self.__speed, ' 5 step')


auto = Car('BMW', 'e28', 1985)
auto.up_speed()
auto.check_speed()
auto.up_speed()
auto.stop_car()
auto.up_speed()
auto.up_speed()
auto.start_engine()
auto.up_speed()
