import turtle as t1
from turtle import *

# t1= turtle.Turtle

color("purple")
t1.bgcolor("black")
t1.speed(1)
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

penup()
setheading(270)
fd(30)
setheading(180)
fd(10)
setheading(0)
pendown()
color("red")

begin_fill()
left(70)
fd(210)
circle(80,200)
right(140)
circle(80,200)
fd(210)
end_fill()


# t1.hideturtle()
def txt():
    penup()
    setheading(120)
    fd(200)
    color("white")
    setheading(30)
    write('I love PYTHON >>>>3',font=("Comic Sans MS",14,"italic"))
txt()

color("white")
pensize(7)
penup()
seth(220)
fd(100)

pendown()
fd(150)
seth(70)
fd(50)
back(50)
seth(0)
fd(50)
back(50)


penup()
seth(220)
back(600-18)

pendown()

back(100)
pensize(2)
begin_fill()
color("white")
seth(265)
back(70)
seth(300)
fd(50)
seth(335)
fd(50)
end_fill()
t1.done()