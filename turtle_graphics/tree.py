import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(0)

# Set the turtle's background color
turtle.bgcolor("black")

# Move the turtle to the starting position
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw the tree trunk
t.setheading(90)
t.forward(100)

# Draw the tree branches
for i in range(1, 10):
    t.setheading(90 - i * 10)
    t.forward(i * 10)
    t.backward(i * 10)

# Draw the star
t.setheading(0)
t.forward(50)
t.right(45)
t.forward(25)
t.left(45)
t.forward(25)
t.right(45)
t.forward(50)

# Finish the drawing
t.end_fill()

# Close the turtle window
turtle.done()