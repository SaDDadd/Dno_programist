import turtle
turtle.write('Hello')  # пишет на экране
# скорость (0-всё нарисуется мгновенно) (1-самая медленная, 10-самая быстрая)
turtle.speed(6)
turtle.setup(640, 420)  # задает размер окна(Ширина,Высота)
turtle.bgcolor('GREEN')  # цвет фона
turtle.pensize(5)  # размер пера
turtle.color('RED')  # цвет черепахи
turtle.dot()  # точка
turtle.hideturtle()  # черепаху убираем
turtle.circle(100)  # рисуем круг
turtle.showturtle()  # черепаха появляется
turtle.clear()  # стирает рисунки
turtle.color('BLACK')
turtle.forward(100)  # вперед
turtle.penup()  # поднять перо
turtle.clearscreen()  # все стирает и возвращает черепаху
turtle.forward(100)
turtle.color('ORANGE')
turtle.pendown()  # опустить перо
turtle.forward(100)
turtle.setheading(90)  # повернуть на 90 градусов относительно оси ОХ
turtle.forward(30)
turtle.setheading(180)
turtle.forward(200)
turtle.reset()  # стирает рисунки и возвращает черепаху
turtle.goto(0, 100)  # перемещает в заданную координату
turtle.goto(-100, 0)
turtle.goto(0, 0)
turtle.fillcolor('BLUE')  # цвет заливки
turtle.begin_fill()  # для заполнения фигуры цветом
turtle.circle(50)
turtle.end_fill()  # для заполнения фигуры цветом
# выводит окно, в котором мы задаем значение
radius = turtle.numinput('Данные', 'Радиус')
turtle.circle(radius)  # из значения делает круг
# default-для ввода в окно minval-мин значение maxval-максимально
num = turtle.numinput('Ввод', 'от 1 до 20', default=5, minval=1, maxval=20)
turtle.circle(num)
# строка для вывода на экран символов
a = turtle.textinput('Ввод', 'Введите число')
print(a)
turtle.done()  # чтобы окно не закрывалось
