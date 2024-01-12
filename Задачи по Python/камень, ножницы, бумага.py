import random
print('Камень ножницы бумага')
print('1=камень, 2=ножницы, 3=бумага')
kam = 1
nog = 2
bum = 3


def main():
    while True:
        a = random.randint(1, 3)
        b = 3
        if a == kam and b == nog:
            print(a)
            print('Проиграл')
        elif a == kam and b == bum:
            print(a)
            print('Победил')
        elif a == nog and b == kam:
            print(a)
            print('Победил')
        elif a == nog and b == bum:
            print(a)
            print('Проиграл')
        elif a == bum and b == kam:
            print(a)
            print('Проиграл')
        elif a == bum and b == nog:
            print(a)
            print('Победил')
        elif a == b:
            print(a)
            print('Ничья')


main()
