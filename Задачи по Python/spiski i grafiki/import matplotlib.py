#import matplotlib
#Есть несколько вариантов вызова пакета matplotilib
#1
#import matplotlib.pyplot
#функции юудут писаться так,
#matplotlib.pyplot.plot(аргумент)
#2
#import matplotlib.pyplot as plt
#Эта инструкция делает псевдоним для пакета plt
#plt.prot(аргумент)
import matplotlib.pyplot as plt


#функция plot используется для создания линейных графикоф
#чтобы вывести на экроан график нужно вызвать функцию plt.show()
# для его создания нужно сделать два списка с указанием координат точек X и Y
def main():
    x_coor = [0, 1, 2, 3, 4]
    y_coor = [0, 3, 4, 1, 6]
    plt.plot(x_coor, y_coor, marker='o')  #создам график
    #marker='o' в каждой вершине ставит точки
    #какие точки(marker) бывают смотреть в файле Marker
    plt.title('Данные')  #Заголовок(plt.title)
    plt.xlabel('Ось х')  #Заголовки для осей(plt.xlabel)
    plt.ylabel('Ось у')  #Заголовок для осей(plt.ylabel)
    plt.xticks(
        [0, 2, 4, 6, 8, 10],
        [2016, 2017, 2018, 2019, 2020, 2021
         ])  #что будет записываться под каждым значением (x) (plt.xticks)
    plt.yticks(
        [0, 2, 4, 6, 8, 10],
        ['$0m', '$2m', '$4m', '$6m', '$8m', '$10m'
         ])  #что будет записываться под каждым значением (y) (plt.yticks)
    plt.grid()  #Добавить сетку(pls.grid)
    plt.xlim(
        xmin=0, xmax=10
    )  #Задает максимальные и минимальные значения графика по x(plt.xlim)
    plt.ylim(
        ymin=0, ymax=10
    )  #Задает максимальные и минимальные значения графика по y(plt.ylim)
    plt.show()  #выводит график


main()