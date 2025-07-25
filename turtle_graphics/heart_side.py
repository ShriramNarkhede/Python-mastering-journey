import random
import time
import turtle

t=turtle.Turtle()

s=turtle.Screen()
s.title("stars")
turtle.bgcolor("black")
t.pencolor("white")
t.hideturtle()

turtle.speed(0)




t.pensize(1)
t.color("pink")
t.penup()
t.setheading(270)
t.fd(100)
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


turtle.done()