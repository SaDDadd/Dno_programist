Days = 5  #количество дней


def main():
    sales = [0] * 5  #создаем список из 5 значений
    print('Продажи в день')
    for index in range(len(sales)):  #пока есть значения в списке
        sales[index] = float(
            input(f'День{index+1}:'))  #переменная[место в списке]
    print('Вы ввели')
    for value in sales:  #пока в списке есть записанные зарплаты
        print(value)  #записываем зарплату


main()