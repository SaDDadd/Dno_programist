def main():
    numbers = [122, 345, 12, 243, 66, 287]
    num = int(input('Введите номер:'))
    if num in numbers:
        print('Есть такой номер')
    else:
        print('Не найдено')


main()