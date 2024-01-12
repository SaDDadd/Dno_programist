import random


def main():
    again = 'y'
    print('Бросаем монету')
    while again == 'y' or again == 'Y':
        a = random.randint(1, 2)
        if a == 1:
            print('Орел')
        else:
            print('Решка')
        again = input('Будете кидать? Напишите Y или y:')


main()
