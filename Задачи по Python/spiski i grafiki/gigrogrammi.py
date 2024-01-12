#создание гистограммы
import matplotlib.pyplot as plt


def main():
    x_coor = [0, 10, 20, 30, 40]
    y_coor = [100, 200, 300, 400, 500]
    schirina_stol = 10  #переменная, которая задает ширину столба
    plt.bar(x_coor, y_coor, schirina_stol,
            color=('r', 'g', 'b', 'm', 'k'))  #plt.bar для создания гистограмм
    #переменная  schirina_stol задает ширину столбов
    #color=() здает цвет для каждого столба. Смотреть файл Color
    plt.title('Данные')  #Заголовок(plt.title)
    plt.xlabel('Год')  #Заголовки для осей(plt.xlabel)
    plt.ylabel('Продажи')  #Заголовок для осей(plt.ylabel)
    plt.xticks(
        [5, 15, 25, 35, 45],
        [2016, 2017, 2018, 2019, 2020
         ])  #что будет записываться под каждым значением (x) (plt.xticks)
    plt.yticks(
        [0, 100, 200, 300, 400, 500],
        ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'
         ])  #что будет записываться под каждым значением (y) (plt.yticks)
    plt.show()


main()