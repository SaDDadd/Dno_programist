import circle
import prim
one = 1
two = 2
thi = 3
fore = 4
b = 5
again = 0


def main():
    menu()
    a = int(input(f'{"Введи число:":>17}'))
    if a == one:
        radius = float(input(f'{"Введите радиус:":>19}'))
        print(f'{"Площадь равна:":>17}', circle.area(radius))
    elif a == two:
        radius = float(input(f'{"Введите радиус:":>19}'))
        print(f'{"Длина окружности равна:":>18}', circle.dlina_okr(radius))
    elif a == thi:
        width = float(input(f'{"Введите ширину:":>19}'))
        ligth = float(input(f'{"Введите длину:":>19}'))
        print(f'{"Площадь прямоугольника равна:":>17}',
              prim.area(width, ligth))
    elif a == fore:
        width = float(input(f'{"Введите ширину:":>19}'))
        ligth = float(input(f'{"Введите длину:":>19}'))
        print(f'{"Периметр равен:":>18}', prim.perimetr(width, ligth))


def menu():
    print(f'{"Меню":^25}')
    print(f'{"Площадь круга=1":^25}')
    print(f'{"Длина окружности=2":^25}')
    print(f'{"Площадь прямоугольника=3":^25}')
    print(f'{"Периметр прямоугольника=4":^25}')
    print(f'{"Чтобы выйти нажмите(5)":^25}')


while again != b:
    main()
    again = int(input('Хотите закончить? Нажмите (5):'))
