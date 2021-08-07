class Car:
    speed = 0

    def ready(self):
        print(self.speed, ' km/h')

    def go(self):
        self.speed += 20
        print(self.speed, ' km/h')

    def stop(self):
        self.speed = 0
        print(self.speed, ' km/h')

    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year


car_1 = Car('BMW', 'E28', 1985)

print(car_1.mark)
print(car_1.model)
print(car_1.year)
car_1.ready()
car_1.go()
car_1.go()
car_1.go()
car_1.go()
car_1.stop()
car_1.go()
car_1.go()
car_1.go()
car_1.stop()
car_1.go()


class Alphabet:

    def print_letters(self):
        print(self.letters)

    def len_letter(self):
        print(len(self.letters))

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters


letters2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alpha_let = Alphabet('eng', letters2)

print(alpha_let.lang)
print(alpha_let.letters)

alpha_let.print_letters()
alpha_let.len_letter()
