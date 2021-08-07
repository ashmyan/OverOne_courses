class Dog:
    def bark(self):  # методы класса
        print('Woof')

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def __init__(self, height, weight, name, age, owner):  # атрибуты класса
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__owner = owner

    def change_name(self, name):
        self.__name = name

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name2):
        self.__name = new_name2


dog_1 = Dog(30, 15, 'Jora', 3, 'Jhon')

dog_1.change_name('Kok')

dog_1.get_owner()
print(dog_1.get_owner())
dog_1.set_owner('Bob')
print(dog_1.get_owner())
print(dog_1.name)
dog_1.name = 'Lucky'
print(dog_1.name)
