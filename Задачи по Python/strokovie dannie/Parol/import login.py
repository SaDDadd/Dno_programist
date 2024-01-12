import login


def main():
    passvord = input('Введите пароль:')
    while not login.valid_password(passvord):
        print('Пароль недоступен')
        passvord = input('Введите пароль:')
    print('Пароль доступен')


main()