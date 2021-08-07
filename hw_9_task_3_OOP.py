class Tomato:
    states = ['Pod', 'Green', 'Yellow', 'Ripe']

    def __init__(self):
        self._state = Tomato.states[0]

    def get_state(self):
        return self._state

    def grow(self):
        for i, k in enumerate(Tomato.states):
            if k == self._state and self._state != Tomato.states[-1]:
                self._state = Tomato.states[i + 1]
                break
        return self._state

    def is_ripe(self):
        if self._state == 'Ripe':
            print("Время собирать урожай!")
        else:
            print("Томат еще не созрел!")

    def __str__(self):
        return f'Томат на стадии: {self._state}'


class TomatoBush:

    def __init__(self, tomatoes, tomato):

        self._tomatoes = []
        for i in range(tomatoes):
            self._tomatoes.append(tomato)

    def all_grow(self):
        for i in self._tomatoes:
            i.grow()
            return self._tomatoes

    def all_ripe(self):
        for i in self._tomatoes:
            if i == 'Ripe':
                return True
            else:
                return False

    def give_away_all(self):
        for i in self._tomatoes:
            i.is_ripe()

    def tomato(self):
        for i in self._tomatoes:
            print(i.get_state())


class Gardener:

    def __init__(self, name, tomato):
        self.name = name
        self._plant = tomato

    def get_plant(self):
        return self._plant

    def work(self):
        return self._plant.grow()

    def plant_tomatoes(self):
        return self._plant._state

    def harvest(self):
        print(f'{self.name} осмотрел помидоры они на стадии {self._plant._state}.')
        if self._plant._state == 'Ripe':
            harvest = input('Хотите собрать урожай?Yes/No')
            if harvest.lower() == 'yes':
                self._plant._state = 'Empty soil'
                plant = input('Хотите посадить еще помидоры?Yes/No')
                if plant.lower() == 'yes':
                    self._plant._state = 'Pod'
                    return self._plant
                else:
                    self._plant._state = 'Empty soil'
                    return self._plant._state
            else:
                return 'Следите за ними, они могут перезреть.'
        else:
            return 'Помидорам нужно еще дозреть. Попробуйте их еще полить.'


tomato_1 = Tomato()
# print(tomato_1.grow())
# print(tomato_1.is_ripe())
# print(tomato_1.grow())
# print(tomato_1.__str__())
# print(tomato_1.is_ripe())

tomatoes = TomatoBush(5, tomato_1)
print(tomatoes.all_grow())
print(tomatoes.all_grow())
tomatoes.tomato()
tomatoes.give_away_all()

gardener = Gardener('Jack', tomato_1)
# print(gardener.name)
# print(gardener.get_plant())
# print(gardener.work())
# print(gardener.work())
# print(gardener.work())
# print(gardener.harvest())
# print(gardener.work())
# print(gardener.work())
