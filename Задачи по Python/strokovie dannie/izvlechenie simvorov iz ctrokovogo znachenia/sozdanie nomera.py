import login


def main():
    nam = input('Введите имя:')
    fam = input('Введите фамилию:')
    nom = input('Введите номер:')
    print('Имя для входа:', login.get_name(nam, fam, nom))


main()