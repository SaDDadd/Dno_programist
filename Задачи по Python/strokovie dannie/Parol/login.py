def get_name(name, famil, nomer):
    first = name[0:3]
    second = famil[0:3]
    fird = nomer[-3:]
    login = first + second + fird
    return login


def valid_password(passvord):
    correct_lenght = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if 6 < len(passvord):
        correct_lenght = True
        for ch in passvord:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
    if correct_lenght and has_uppercase and has_lowercase and has_digit:
        is_value = True
    else:
        is_value = False
    return is_value