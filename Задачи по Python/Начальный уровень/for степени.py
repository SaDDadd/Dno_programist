first = int(input())
end = int(input())
a = '--------------'

print('Число\t Квадрат числа')
print()
print(f'{a:^20}')

for kv in range(first, end+1):
    num = kv**2
    print(f'{kv:^10} {num:^10}')
