def main():
    text = 'gdfm ghjdsg jhsd'
    list = text.split()
    print(list)


main()


def main():
    date = '09/10/2007'
    list = date.split(
        '/')  #split(символ разделения)-разделяет список символом в скобках
    print(f'День:{list[0]}')
    print(f'Месяц:{list[1]}')
    print(f'Год:{list[2]}')


main()
