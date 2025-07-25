import random
import time
import turtle

t=turtle.Turtle()

s=turtle.Screen()
s.title("TCOER")
turtle.bgcolor("black")
t.pencolor("white")
# t.hideturtle()

turtle.speed(1)







t.penup()
t.backward(500)
t.pendown()


t.pencolor("purple")
t.penup()
t.backward(100)
t.pendown()
t.pensize(3)
t.setheading(90)
t.forward(100)

t.setheading(0)
t.forward(90)
t.backward(180)
t.forward(90)
t.setheading(270)
t.fd(200)
t.setheading(180)
t.fd(90)
t.backward(180)
t.penup()


t.setheading(0)
t.fd(140)
t.setheading(270)
t.fd(40)






# hearts
t.pendown()
t.pensize(3)
t.pensize(1)
t.color("red")
t.penup()
t.setheading(0)
# t.fd(100)
t.setheading(0)
t.pendown()
t.begin_fill()
t.left(50)
t.fd(190)
t.circle(70,200)
t.right(140)
t.circle(70,200)
t.fd(190)
t.end_fill()

t.penup()
t.setheading(0)
t.fd(220)


t.setheading(90)
t.fd(10)
t.pendown()



t.pensize(7)

t.color("orange")
t.fd(30)
#t
t.fd(200)
t.setheading(0)
t.forward(90)
t.backward(180)
t.forward(90)
t.setheading(270)
t.fd(200)

t.penup()
t.setheading(0)
t.fd(200)
t.setheading(90)
t.fd(200)


#c
t.color("indigo")
t.pendown()
t.pensize(7)
t.setheading(180)
t.circle(110,190)

t.penup()
t.setheading(0)
t.fd(120)

#0
t.color("blue")
t.pensize(7)
t.pendown()
t.circle(110,360)

t.penup()
t.fd(150)
#e
t.color("yellow")
t.pensize(7)
t.pendown()
# t.color("red")
t.setheading(0)
#t.forward(10)
t.pendown()
t.setheading(90)
t.fd(200)
t.setheading(0)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.penup()


#r
t.color("pink")
# t.color("red")
t.setheading(0)
t.forward(50)
t.pendown()
t.setheading(90)
t.forward(200)
t.setheading(270)
t.forward(100)
t.setheading(0)
t.circle(55,180)
t.setheading(270)
t.forward(100)
t.setheading(310)
t.forward(140)
t.penup()

#border

t.pensize(9)

t.color("white")
t.fd(50)
t.setheading(0)
t.forward(50)
t.pendown()
t.setheading(90)
t.forward(300)
t.setheading(0)
t.back(1400)
t.setheading(270)
t.forward(300)
t.setheading(0)
t.forward(1400)


turtle.done()