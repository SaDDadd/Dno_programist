
def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales*comm_rate-advanced_pay
    print(pay)
    if pay < 0:
        print('Возместить разницу')


def get_sales():
    monthly_sales = float(input('Ввести сумму продаж:'))
    return monthly_sales


def get_advanced_pay():
    advanced = float(input('Ввести сумму аванса:'))
    return advanced


def determine_comm_rate(sales):
    if sales < 10000:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999:
        rate = 0.16
    else:
        rate = 0.18
    return rate


a = 'д'
while a == 'д' or a == 'Д':
    main()
    a = input('Продолжить?')
