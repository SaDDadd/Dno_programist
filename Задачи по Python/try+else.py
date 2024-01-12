def main():
    total = 0
    try:
        fail = open("Fail.txt", "r")
        for line in fail:
            amound = float(line)
            total += amound
        fail.close()
    except Exception as err:  # для отлавливания всех исключений
        print(err)
    else:  # для алтернативного исхода
        print(total)


main()
