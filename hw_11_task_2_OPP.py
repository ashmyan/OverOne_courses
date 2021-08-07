class Dog:
    def bark(self):
        print('Woof')

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def __init__(self, height, weight, name, age, owner):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__owner = owner

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner


dog = Dog(30, 15, 'Jora', 3, 'Jhon')

dog.name = 'Luck'
dog.height = 35
dog.weight = 21
dog.age = 7
dog.owner = 'Sasha'

print(dog.name)
print(dog.height)
print(dog.weight)
print(dog.age)
print(dog.owner)
