a = 'Hello ЧМО'
for i in range(6):  # Цикл (любая переменная) in range(6)диапозон
    print(a)
a = 'Hello ЧМО'
for i in range(1, 6):  # range(1, 6)диапозон от 1 до 6 повторений (шестое повторение не происходит)
    print(a)
b = 0
a = 'Hello!'
for i in a:
    if i == 'l':  # Если в a есть l, то b будет написано столько раз, сколько есть l
        b += 1  # Если условие выполняется, то к b + 1
print(b)

a = 5
while a < 10:  # While цикл
    print(a)
    a += 2
a = True
while a:
    if input('_') == 'stop':  # Бесконечный ввод, пока мы не напишем stop
        a = False
for i in range(1, 11):
    if i == 5:
        break  # break позволяет выйти из цикла
    if i % 2 == 0:
        continue  # continue начинает цикл заново до конца задачи или (break)

    print('i')
a = None  # None значение ничего
for i in 'hello':
    if i == 'l':
        a = True
        break  # Как только мы находим нужную переменную, то мы выходим из цикла
else:
    a = False


print(a)
