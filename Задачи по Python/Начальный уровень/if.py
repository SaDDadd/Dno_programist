a = int(input())

isHappy = False
# Если isHappy False, то  print('+') пропускаем, елси True, то остальной код игнорируется
if isHappy:
    print('+')
# Если a == 5, то остальной код игнорируется, not a==5, то print(5) пропускается
elif a == 5:
    print(5)
# Если a == 7, то остальной код игнорируется, not a==7, то print(5) пропускается
elif a == 7:
    print(7)
else:
    print('-')
if isHappy and a == 5:  # Чтобы выполнилась функция, нужно чтобы isHappy and a==5
    print('yes')
if isHappy or a == 5:  # Чтобы выполнилась функция, нужно чтобы isHappy or a==5
    print('yes')

# Также if можно записать короче
a = input()
number = 5 if a == 10 else 0
print(number)
