import turtle

b=10
t1=turtle.Turtle()
t1.speed(0)
turtle.bgcolor("black")
t1.pensize(1)
t1.color("blue")
#t1.speed()
t1 .penup()
t1.setheading(180)
t1.forward(160)
t1.pendown()
for i in range(30):
 
  t1.setheading(45+50) 
  
  t1 .fd (150+b)
 # b=b+10
  t1.setheading(315)
  t1.fd(150)  
  t1.setheading(180)
  t1.forward(210+b)
  
t1.setheading(0)
t1.forward(210+b) 


for a in range(30):
 t1.color("red")
 t1.setheading(45)
 t1 .back(150+b)

 t1.setheading(315)
 t1.back(150)
 t1.setheading(180)
 t1.back(210+b)

#for i in range(15):
 



turtle.done()