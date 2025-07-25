import turtle

t=turtle.Turtle()
t.speed(0.05)



a=3
b=3
c=3
turtle.bgcolor("black")
for i in range (73):
      c=(90+a)
      t.pensize(1)
      t.pencolor("blue")
      t.setheading(120+a)
      t.circle(120)
      t.home()
      a=a+5
    
      
      
for i in range (73):
      t.pensize(2)
      t.pencolor("red")
      t.setheading(90+c)
      t.circle(90)
      t.home()    
      c=c+5

for i in range (73):
      t.pencolor("green")
      t.right(90+b)
      t.circle(270,5)
      t.home()
      b=b+5


  



turtle.done()