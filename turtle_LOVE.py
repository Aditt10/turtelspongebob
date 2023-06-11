import turtle


turtle.speed(2)
turtle.bgcolor("white")
turtle.pensize(3)

def fun():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
    
turtle.color("red","pink")
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)


fun()
turtle.left(120)

fun()

turtle.forward(111.65)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
