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
def star():
    t.penup()
    t.setheading(270)
    t.fd(100)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.left(50)
    t.fd(70)
    t.circle(25,200)
    t.right(140)
    t.circle(25,200)
    t.fd(70)
    t.end_fill()



s.colormode(255)
while True:
 
 x=random.randint(-400,250)
 y=random.randint(-400,250)
 r=random.randint(0,255)
 g=random.randint(0,255)
 b=random.randint(0,255)
 t.pencolor(r,g,b)
 t.penup()
 t.goto(x,y)
 star()
      
      


turtle.done()