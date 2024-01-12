#модуль
def get_name(name, famil, nomer):
    first = name[0:3]
    second = famil[0:3]
    fird = nomer[-3:]
    login = first + second + fird
    return login
