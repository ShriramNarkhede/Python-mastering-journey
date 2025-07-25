import turtle
from turtle import *

color("red")
turtle.bgcolor("black")
begin_fill()
pensize(1)
speed(0)
a=0
b=0
while True:
      begin_fill()
     
      left(50)
      fd(133)
      circle(50,200)
      right(140)
      circle(50,200)
      fd(133)
      end_fill()
      a=a+1
      b=b+1
      fd(10+b)
       
     
penup()
color("white")
setheading(270)
fd(50)
setheading(180)
fd(50)
pensize(5)

write("Only for you darling ",False,left,"Arial")

turtle.done()