def main():
    try:
        while numb != 5:
            numb = int(input("Введи число:"))
            if numb > 5:
                print("Попробуй чуть меньше")
            elif numb < 5:
                print("Попробуй чуть меньше")
            else:
                print("Ты победил")
    except:
        print("Произошел сбой")
    finally:  # всегда выполняются(даже во время ошибки)
        print("Надеюсь еще увидимся")


main()
