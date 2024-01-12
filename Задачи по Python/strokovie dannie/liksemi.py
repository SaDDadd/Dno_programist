def main():
    text_1 = 'один два три'  #строковые литералы
    text_2 = '10:20:30:40'
    text_3 = 'a/b/c/d'

    display_tokens(text_1, ' ')  #
    print()
    display_tokens(text_2, ':')  #
    print()
    display_tokens(text_3, '/')  #


def display_tokens(data,
                   delimiter):  #функция, которая принимает data, delimiter
    tokens = data.split(
        delimiter
    )  #переменная, которая разделяет части литерала, указанным разделителем(delimiter)
    for item in tokens:  #пока есть части в строковом литерале
        print(f'Лексема: {item}'
              )  #записывает отдельные части строковых литералов


main()
