import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create and customize the turtle
t = turtle.Turtle()
t.pensize(5)
t.color("blue")
t.speed(3)

# Function to move turtle without drawing
def move_without_drawing(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw letter H
move_without_drawing(-200, 100)
t.setheading(270)
t.forward(200)
move_without_drawing(-200, 0)
t.setheading(0)
t.forward(80)
move_without_drawing(-120, 100)
t.setheading(270)
t.forward(200)

# Draw letter E
move_without_drawing(-80, 100)
t.setheading(0)
t.forward(80)
move_without_drawing(-80, 100)
t.setheading(270)
t.forward(200)
move_without_drawing(-80, 0)
t.setheading(0)
t.forward(80)
move_without_drawing(-80, 50)
t.forward(60)

# Draw letter L
move_without_drawing(40, 100)
t.setheading(270)
t.forward(200)
t.setheading(0)
t.forward(80)

# Draw letter L
move_without_drawing(160, 100)
t.setheading(270)
t.forward(200)
t.setheading(0)
t.forward(80)

# Draw letter O
move_without_drawing(280, 100)
t.setheading(270)
t.forward(200)
t.setheading(0)
t.forward(80)
t.setheading(90)
t.forward(200)
t.setheading(180)
t.forward(80)

# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
