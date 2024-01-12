Max = 6
total = 0.0
print(f'{"Сумма из 6 чисел":^20}')
for sum in range(Max):
    num = int(input(f'{"Введи число:":>15}'))
    total = total+num
print(f'{"Суммма равна=":>15}', end="")
print(total)
