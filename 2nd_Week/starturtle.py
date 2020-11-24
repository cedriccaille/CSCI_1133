import turtle
def star(xpos, ypos):
    turtle.penup()
    turtle.setpos(xpos,ypos)
    turtle.pendown()
    turtle.left(36)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)

star(100, 100)

star(0, 0)

star(-100, 0)

star(-100, 100)
