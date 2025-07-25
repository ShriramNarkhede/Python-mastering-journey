import random
import turtle

t=turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a=0
b=0
t.speed(0)
t.penup()
s.colormode(255)

t.goto(0,200)
t.pendown()
# s.colormode(210)
# while True:
 
while True:
      # x=random.randint(-400,250)
      # y=random.randint(-400,250)
      
      t.fd(a)
      t.right(b)
      a+=3
      b+=1
    


      if b==210:
            break
      t.hideturtle()
turtle.done()