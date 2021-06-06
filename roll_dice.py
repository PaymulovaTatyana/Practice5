from random import randint
import time

def input_name():
    igrok1=input('Введите имя 1-го играющего ')
    igrok2= input('Введите имя 2-го играющего ')
    return[igrok1, igrok2]

def game(names):
    n = input('Введите количество партий ')
    sum1 = 0
    sum2 = 0
    for i in range(int(n)):
        print('Номер партии: ', i + 1)
        print('Кубик бросает', names[0])
        time.sleep(1)
        n1 = randint(1, 6)
        sum1 = sum1 + n1
        print('Выпало:', n1, 'Сумма1=', sum1)

        print('Кубик бросает', names[1])
        time.sleep(1)
        n2 = randint(1, 6)
        sum2 = sum2 + n2
        print('Выпало:', n2, 'Сумма2=', sum2)
    return [sum1, sum2]

def selection_winner(sum12,names):
    if sum12[0] > sum12[1]:
        print('Выиграл', names[0])
        print('Сумма баллов', sum12[0])
    elif sum12[0] < sum12[1]:
        print('Выиграл', names[1])
        print('Сумма баллов', sum12[1])
    else:
        print('Ничья')
        print('Сумма баллов', sum12[0])