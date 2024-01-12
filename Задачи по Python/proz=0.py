proz = 0.20


def main():
    reg_price = obichn()
    otpysk = reg_price-discount(reg_price)
    print(otpysk)


def obichn():
    price=float(input('Введите цену:'))
    return price


def discount(price):
    return price * proz


main()
