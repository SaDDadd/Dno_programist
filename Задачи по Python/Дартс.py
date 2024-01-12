import turtle
x = 30
sila = 20
turtle.setup(700, 700)
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.forward(x)
turtle.setheading(90)
turtle.forward(x)
turtle.setheading(180)
turtle.forward(x)
turtle.setheading(270)
turtle.forward(x)
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(90)
turtle.showturtle()
turtle.pendown()
while True:
    speed = turtle.numinput('Скорость', 'От 1 до 10',
                            default=5, minval=1, maxval=10)
    ugol = turtle.numinput('Ввод', 'Угол', default=5, minval=1, maxval=999)
    turtle.setheading(ugol)
    dist = sila*speed
    turtle.forward(dist)
    turtle.setheading(ugol)
    if (turtle.xcor() >= 100 and turtle.xcor() <= (100+x) and turtle.ycor() >= 100 and turtle.ycor() <= (100+x)):

        a = turtle.xcor()
        b = turtle.ycor()
        turtle.fillcolor('RED')
        turtle.begin_fill()
        turtle.speed(0)
        turtle.goto(100, 100)
        turtle.goto(100, 130)
        turtle.goto(130, 130)
        turtle.goto(130, 100)
        turtle.goto(100, 100)
        turtle.goto(a, b)
        turtle.end_fill()
        turtle.write('МОЛОДЕЦ')
        break
    else:
        turtle.goto(0, 0)
        turtle.setheading(90)
