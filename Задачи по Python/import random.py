import random


def main():
    again='y'
    while again == 'y' or again == 'Y':
        print('Бросаем куб')
        print(f'{random.randint(1,6)}')
        again = input('Бросить еще? Напиши Y или y:')


main()
