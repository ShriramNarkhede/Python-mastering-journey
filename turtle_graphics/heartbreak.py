import turtle as t1
from turtle import *


color("red")
t1.bgcolor("black")
t1.speed(1)
pensize(1)

penup()
setheading(270)
fd(100)
setheading(0)
pendown()
begin_fill()
left(40)
fd(180)
circle(90,200)

right(120)
circle(90,200)
fd(180)

end_fill()

color("black")
pensize(5)
seth(70)

fd(30)
pensize(6)
fd(30)
pensize(8)
fd(30)
pensize(10)
fd(30)
pensize(12)
fd(30)


seth(190)
fd(70)
penup()
fd(70)
pendown()
color("white")
write('World Cup 😖',font=("Comic Sans MS",20,"italic"))
penup()
back(70)
pendown()
color("black")
seth(80)
fd(110)


done()

