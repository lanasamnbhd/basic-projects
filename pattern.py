import turtle as tu

roo=tu.Turtle()
wn=tu.Screen()
wn.bgcolor("black")
wn.title("fractal free pattern")
roo.left(90)
roo.speed(20)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(1)
        roo.left(30)
        draw(3 * 1 / 4)
        roo.right(60)
        draw(3 * 1 / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)


draw(20)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("brown")
        roo.forward(1)
        roo.left(30)
        draw(3 * 1 / 4)
        roo.right(60)
        draw(3 * 1 / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(20)

roo.left(270)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")
        roo.forward(1)
        roo.left(30)
        draw(3 * 1 / 4)
        roo.right(60)
        draw(3 * 1 / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(20)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("#FFF8DC")
        roo.forward(1)
        roo.left(30)
        draw(3 * 1 / 4)
        roo.right(60)
        draw(3 * 1 / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(20)

###############################################
def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("lightgreen")
        roo.forward(1)
        roo.left(30)
        draw(4 * 1 / 5)
        roo.right(60)
        draw(4 * 1 / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(1)

draw(40)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")
        roo.forward(1)
        roo.left(30)
        draw(4 * 1 / 5)
        roo.right(60)
        draw(4 * 1 / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(1)

draw(40)

roo.right(270)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")
        roo.forward(1)
        roo.left(30)
        draw(4 * 1 / 5)
        roo.right(60)
        draw(4 * 1 / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(1)

draw(40)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("#FFF8DC")
        roo.forward(1)
        roo.left(30)
        draw(4 * 1 / 5)
        roo.right(60)
        draw(4 * 1 / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(1)

draw(40)

######################################

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("cyan")
        roo.forward(1)
        roo.left(30)
        draw(6 * 1 / 7)
        roo.right(60)
        draw(6 * 1 / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(60)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(1)
        roo.left(30)
        draw(6 * 1 / 7)
        roo.right(60)
        draw(6 * 1 / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(60)

roo.right(270)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")
        roo.forward(1)
        roo.left(30)
        draw(6 * 1 / 7)
        roo.right(60)
        draw(6 * 1 / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(60)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("FFF8DC")
        roo.forward(1)
        roo.left(30)
        draw(6 * 1 / 7)
        roo.right(60)
        draw(6 * 1 / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(1)

draw(60)

wn.exitonclick()




