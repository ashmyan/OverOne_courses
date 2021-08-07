class Animal:
    def __init__(self, name, age, owner):
        self.__name = name
        self.__age = age
        self.__owner = owner

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    def birthday(self):
        if self.__age > 5:
            print(self.__name + " sleeping all day.")
        else:
            print(self.__name + ' running and jumping 24/7')

    def owner_name(self):
        print(self.__owner, ' owner is ', self.__name)


animal = Animal('Ruby', 2, 'Sasha')

animal.age = 4
animal.owner = 'Stas'
animal.name = 'Barry'
print(animal.age)
print(animal.name)
print(animal.owner)
animal.owner_name()
animal.birthday()
animal.age = 6
animal.birthday()
