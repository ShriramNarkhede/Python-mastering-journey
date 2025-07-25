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
      t.setheading(30+a)
      t.fd(90)
      t.setheading(60+a)
      t.fd(90)
      t.setheading(10+a)
      t.fd(90)
      t.setheading(15+a)
      t.fd(90)

      t.home()
      a=a+5
    
      
      
for i in range (73):
      t.pensize(2)
      t.pencolor("purple")
      t.setheading(90+c)
      t.backward(50)
      t.setheading(270+c)
      t.backward(50)
      t.home()    
      c=c+5

# for i in range (73):
#       t.pencolor("green")
#       t.right(90+b)
#       t.circle(270,5)
#       t.home()
#       b=b+5


  



turtle.done()
