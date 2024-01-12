import turtle

turtle.setup(640, 640)
turtle.speed(1)
first_circle = turtle.numinput('Радиус круга', 'От 50 до 100')
second_circle = turtle.numinput('Радиус круга', 'От 30 до 40')
third_circle = turtle.numinput('Радиус круга', 'От 10 до 20')


def main():
    drawBase()
    drawMidSection()
    drawHead()
    drawHat()


def drawBase():
    a = first_circle*2
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(first_circle)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(a)
    turtle.setheading(0)
    turtle.pendown()


def drawMidSection():
    b = second_circle*2
    turtle.circle(second_circle)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(b)
    turtle.setheading(0)
    turtle.pendown()


def drawHead():
    turtle.circle(third_circle)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(third_circle)
    turtle.setheading(0)
    turtle.forward(5)
    turtle.pendown()
    turtle.circle(2)
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(8)
    turtle.setheading(90)
    turtle.forward(2)
    turtle.pendown()
    turtle.circle(2)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(3)
    turtle.setheading(90)
    turtle.forward(7)
    turtle.setheading(0)
    turtle.pendown()


def drawHat():
    turtle.fillcolor('RED')
    turtle.begin_fill()
    turtle.forward(15)
    turtle.setheading(90)
    turtle.forward(10)
    turtle.setheading(180)
    turtle.forward(30)
    turtle.setheading(270)
    turtle.forward(10)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(10)
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.setheading(270)
    turtle.forward(20)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.end_fill()


main()
turtle.done()
