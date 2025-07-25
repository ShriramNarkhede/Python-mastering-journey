import turtle
from tkinter.ttk import Style

t1=turtle.Turtle()
turtle.bgcolor("black")
t1.color("violet")

Style=("Courier",30,'normal')
t1.write('Hello World!!',font=Style,align='center')
t1.hideturtle()
t1.left(270)
t1.penup()
t1.forward(120)
t1.pendown()
t1.circle(120)

turtle.done()