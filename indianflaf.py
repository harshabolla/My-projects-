import turtle 
t =turtle.Turtle()

t.speed(1)
#t.bgcolor('black')
t.pensize(3)
t.color('blue')

def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
draw(0,-80)
t.circle(80, 360)
#een Rectangle
t.color('green')
t.begin_fill()

t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)

t.end_fill()


#Orange Rectangle
t.color('orange')
draw(-350,80)

t.begin_fill()

t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)

t.end_fill()

draw(50,80) 
t.right(80)
t.forward(70)
t.left(9)
t.forward(20)
t.left(9)
t.forward(70)
t.left(9)
t.forward(20)

turtle.done()