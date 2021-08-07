from random import randint

computer = randint(0, 100 + 1)
shance = 0
print("Я загадал число от 1 до 100. У вас пять попыток отгадать его!)")
while shance != 5:
    numb = int(input('Ваше число?\n'))
    if numb != computer and shance == 5:
        print('Вы проиграли, это число:' + str(computer) + ' .Повезет в следующий раз!)')
        shance += 1
    elif 100 > numb > computer:
        shance += 1
        print('Меньше, осталось ' + str(5 - shance) + ' попыток!\n')
    elif 100 > numb < computer:
        shance += 1
        print('Больше, осталось ' + str(5 - shance) + ' попыток!\n')
    elif numb == computer:
        shance = 5
        print("ПОБЕДА!\n")
