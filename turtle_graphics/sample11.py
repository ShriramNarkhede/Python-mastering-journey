import turtle
from turtle import *

t1= turtle.Turtle

color("purple")
turtle.bgcolor("black")

pensize(1)

penup()
setheading(270)
fd(100)
setheading(0)
pendown()
begin_fill()
left(50)
fd(270)
circle(100,200)
right(140)
circle(100,200)
fd(270)
end_fill()
turtle.done()