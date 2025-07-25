import turtle

t1= turtle.Turtle
i=3
a= 10
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("indigo")
turtle.bgcolor("black")
for i in range(5):

  turtle.circle(100+i)
  
  turtle.setheading(270)
  turtle.penup()
  turtle.back(10)
  turtle.pendown()
  turtle.setheading(0)
  
turtle.pencolor("black")

turtle.done()