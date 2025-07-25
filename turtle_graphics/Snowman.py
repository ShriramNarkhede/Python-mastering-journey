import turtle

t=turtle.Turtle()

turtle.bgcolor("light blue")
t.pencolor("white")
t.speed(0)

t.shapesize(2)
t.penup()
t.setheading(180)
t.fd(100)

t.pendown()
t.color("white")
t.begin_fill()
#circle base
t.circle(90)
t.end_fill()

#2nd circle
t.setheading(270)
t.penup()
t.fd(40)

t.pendown()
t.color("white")
t.begin_fill()

t.setheading(0)
t.circle(70)
t.end_fill()


#3rd circle
t.setheading(90)
t.penup()
t.fd(95)

t.pendown()
t.color("white")
t.begin_fill()

t.setheading(0)
t.circle(50)
t.end_fill()


#snowman eyes
t.color("white","black")
t.setheading(90)
t.fd(70)
t.setheading(0)
t.fd(13)
t.begin_fill()
t.circle(7)
t.end_fill()


t.setheading(180)
t.fd(26)
t.setheading(0)
t.begin_fill()
t.circle(7)
t.end_fill()


#mouth
t.color("black","red")


t.penup()
t.fd(13)
t.setheading(270)
t.fd(35)

t.pendown()
t.setheading(0)
t.begin_fill()
t.circle(17)
t.end_fill()

t.color("white")
t.penup()
t.seth(90)
t.fd(6)
t.pendown()
t.setheading(0)

t.begin_fill()
t.circle(17)
t.end_fill()


#t.hideturtle()

t.color("black")




#right hand
t.penup()
t.seth(270)
t.fd(50)

t.seth(0)
t.fd(50)
t.pendown()
t.color("brown")
t.seth(35)
t.pensize(6)
t.fd(90)
t.pensize(3)

#finger
t.seth(100)
t.fd(40)
t.back(40)
t.seth(70)
t.fd(40)
t.back(40)
t.seth(35)
t.fd(40)
t.back(40)

t.back(90)

t.seth(180)
t.penup()
t.fd(100)

#left hand


t.pendown()
t.color("brown")
t.seth(145)
t.pensize(6)
t.fd(90)
t.pensize(3)

#finger
t.seth(105)
t.fd(40)
t.back(40)
t.seth(140)
t.fd(40)
t.back(40)
t.seth(165)
t.fd(40)
t.back(40)

t.setheading(145)
t.back(90)
t.seth(0)
t.penup()
t.fd(50)

t.seth(270)
t.fd(25)
t.seth(0)
t.pendown()

#buttons
t.color("black")
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)

t.penup()
t.fd(50)
t.pendown()

t.seth(0)
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)


t.penup()
t.fd(60)
t.pendown()

t.seth(0)
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)

t.setheading(90)
t.penup()
t.fd(237)
t.color("black")
t.pendown()

#hat
t.seth(0)
t.begin_fill()
t.fd(50)
t.seth(90)
t.fd(10)
t.seth(180)
t.fd(20)
t.seth(90)
t.fd(50)
t.seth(180)
t.fd(60)


t.seth(270)
t.fd(50)

t.seth(180)
t.fd(20)
t.seth(270)
t.fd(10)
t.seth(0)
t.fd(50)

t.end_fill()

t.penup()
t.seth(270)
t.fd(330)
t.pendown()

#t.home()

t.pencolor("black")
t.pensize(15)
t.seth(0)
t.back(90)
t.fd(170)

t.fd(360)
t.penup()

#
#////////////////********************************************************************
#
#////////////////********************************************************************
t.speed(0)
#
#////////////////********************************************************************
t.back(80)
#2nd snowman

t.seth(90)
t.fd(183)

t.seth(180)

t.pensize(1)
t.color("white")
t.begin_fill()
#circle base
t.circle(90)
t.end_fill()

#2nd circle
t.setheading(270)
t.penup()
t.fd(40)

t.pendown()
t.color("white")
t.begin_fill()

t.setheading(0)
t.circle(70)
t.end_fill()


#3rd circle
t.setheading(90)
t.penup()
t.fd(95)

t.pendown()
t.color("white")
t.begin_fill()

t.setheading(0)
t.circle(50)
t.end_fill()


#snowman eyes
t.color("white","black")
t.setheading(90)
t.fd(70)
t.setheading(0)
t.fd(13)
t.begin_fill()
t.circle(7)
t.end_fill()


t.setheading(180)
t.fd(26)
t.setheading(0)
t.begin_fill()
t.circle(7)
t.end_fill()


#mouth
t.color("black","red")


t.penup()
t.fd(13)
t.setheading(270)
t.fd(35)

t.pendown()
t.setheading(0)
t.begin_fill()
t.circle(17)
t.end_fill()

t.color("white")
t.penup()
t.seth(90)
t.fd(6)
t.pendown()
t.setheading(0)

t.begin_fill()
t.circle(17)
t.end_fill()


#t.hideturtle()

t.color("black")




#right hand
t.penup()
t.seth(270)
t.fd(50)

t.seth(0)
t.fd(50)
t.pendown()
t.color("brown")
t.seth(35)
t.pensize(6)
t.fd(90)
t.pensize(3)

#finger
t.seth(100)
t.fd(40)
t.back(40)
t.seth(70)
t.fd(40)
t.back(40)
t.seth(35)
t.fd(40)
t.back(40)

t.back(90)

t.seth(180)
t.penup()
t.fd(100)

#left hand


t.pendown()
t.color("brown")
t.seth(145)
t.pensize(6)
t.fd(90)
t.pensize(3)

#finger
t.seth(105)
t.fd(40)
t.back(40)
t.seth(140)
t.fd(40)
t.back(40)
t.seth(165)
t.fd(40)
t.back(40)

t.setheading(145)
t.back(90)
t.seth(0)
t.penup()
t.fd(50)

t.seth(270)
t.fd(25)
t.seth(0)
t.pendown()

#buttons
t.color("red")
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)

t.penup()
t.fd(50)
t.pendown()

t.seth(0)
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)


t.penup()
t.fd(60)
t.pendown()

t.seth(0)
t.begin_fill()
t.circle(12)
t.end_fill()
t.seth(270)

t.setheading(90)
t.penup()
t.fd(237)
t.color("red")
t.pendown()
# turtle.speed(1)
def cr():
      t.setheading(0)
      t.begin_fill()
      t.color("white")
      t.circle(12)
      t.end_fill()

#hat****************************






t.begin_fill()
t.seth(0)
t.fd(30)
t.seth(100)
t.fd(70)
# cr()


t.color("red")
t.setheading(235)
t.fd(85)
t.seth(0)
t.fd(50)

t.end_fill()
t.seth(90)
t.fd(60)
cr()

t.seth(90)
t.penup()
t.back(60)
t.seth(180)
t.fd(20)

t.pendown()



# turtle.speed(0)
t.penup()
t.seth(270)
t.pencolor("red")
t.fd(30)
# t.hideturtle()
t.pendown()
t.seth(190)
t.pensize(9)
t.fd(10)

t.pensize(7)
t.fd(8)

t.pensize(5)
t.fd(6)
t.penup()
t.seth(0)
t.fd(10)
t.seth(270)
t.fd(300)
t.pendown()

t.turtlesize(3)
#t.home()
# t.pendown()
# t.pencolor("black")
# t.pensize(15)
# t.seth(0)
# t.back(90)
# t.fd(180)

t.penup()
t.fd(250)


#goto()
t.home()

t.penup()
t.fd(80)
t.seth(90)
t.fd(170)
t.pendown()


# t.hideturtle()
def heart():
      
      t.pensize(1)
      t.color("red")
      t.penup()
      t.setheading(270)
      t.fd(100)
      t.setheading(0)
      t.pendown()
      t.begin_fill()
      t.left(50)
      t.fd(115)
      t.circle(40,200)
      t.right(140)
      t.circle(40,200)
      t.fd(115)
      t.end_fill()


heart()
turtle.done()

