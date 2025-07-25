import turtle

t= turtle.Turtle()
s=turtle.Screen()
s.screensize(800,450,"black")
t.pencolor("green")
t.pensize(2)
t.speed(0)
def square():
      # while True:
         for i in range(4):   
            t.fd(150)
            t.left(90)
           

square()
t.left(30)
t.forward(150)
t.right(30)
square()

t.left(90)
t.fd(150)
t.left(90+30)
t.fd(150)

t.right(30+180)
t.fd(150)

t.left(30)
t.fd(150)

t.right(90+30)
t.fd(150)

t.right(60)
t.fd(150)

turtle.done()
