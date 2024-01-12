def main():
    try:  # Основа программы
        hours = int(input("Введите часы:"))
        zena = int(input("Цена за час:"))
        zp = hours * zena
        print("Зарплата:", zp)
    except ValueError:  # Тип ошибки
        print("Ошибка.Вы ввели число с правающей запятой или слово")


main()


def m():
    total = 0
    try:
        fail = open("WERT.txt", "r")
        for line in fail:
            chislo = float(line)
            total += chislo
        fail.close()
        print("Сумма:", total)
    except:  # Так же можно написать без указания типа ошибки
        print("Произошла ошибка")
