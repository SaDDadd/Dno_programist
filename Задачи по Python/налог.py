print(f'{"Номер лота или 0":^20}')
lot = int(input(f'{"Введи номер:":>15}'))
while lot != 0:
    val = float(input(f'{"Стоимость имущ:":>17}'))
    nal = val*0.0065
    print(f'{nal:^20}')
    print(f'{"Введите новый номер":>15}')
    lot = int(input(f'{"Введи номер:":>15}'))
