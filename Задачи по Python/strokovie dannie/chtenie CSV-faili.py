def main():
    fail = open('text.csv', 'r')  #открываем файл
    lines = fail.readlines()  #читаем все строки в файле
    fail.close()  #закрываем файл
    for line in lines:  #пока существуют строки в прочитанном файле
        tokens = line.split(
            ',')  #получаем отчет каждой контрольной (делим строку на части)
        total = 0
        for token in tokens:  #пока есть числа в разделенной строке
            total += float(token)  #к total прибавляем часть строки
        sredn = total / len(
            tokens)  #находим средний балл(total/поочереди каждую часть строки)
        print(f'Средний балл: {sredn}')


main()