class Pet:
    _counter = 0

    def __init__(self, name, age, owner, weight=5, height=2):
        self._name = name
        self._age = age
        self._owner = owner
        self.weight = weight
        self.height = height
        Pet._counter += 1

    def get_counter(self):
        return self._counter

    def voice(self):
        print('Voice')

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

    def run(self):
        print('Runing')

    def jump(self):
        print('Jumping')

    def birthday(self):
        self._age += 1
        return self._age

    def __str__(self):
        return f'Name:{self._name}, age:{self._age}, owner: {self._owner}'


class Dog(Pet):

    def voice(self):
        print('Gaff')

    def jump(self, h):
        if h <= 0.5:
            print('Dog jump')
        else:
            print('Dog cant jump')


class Cat(Pet):
    def voice(self):
        print('Miyy')

    def jump(self, h):
        if h <= 2:
            print('Cat jump')
        else:
            print('Cat cant jump')


class Parret(Pet):
    def voice(self):
        print('Kurlik')

    def jump(self, h):
        if h <= 0.05:
            print('Parret jump')
        else:
            print('Parret cant jump')

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05

    def fly(self):
        if self.weight > 0.2:
            print('Cant fly')
        else:
            print('Fly')


parret_1 = Parret('Lol', 2, 'Pop')
cat_1 = Cat('Bursik', 2, 4)

dog_2 = Dog('Fufel', 1, 'Tor')

parret_1.change_weight()
print(parret_1.birthday())
print(parret_1._owner)
print(parret_1.weight)
print(parret_1.weight)
print(parret_1.height)
parret_1.jumping = 0.02

parret_1.jump(1)
dog_2.jump(0.2)
cat_1.jump(2.1)
dog_2.voice()
cat_1.voice()
parret_1.voice()
animals = [cat_1, dog_2, parret_1]

print(dog_2.get_counter())

for animal in animals:
    animal.voice()

print(parret_1)
print(dog_2)
print(dog_2.get_counter())


