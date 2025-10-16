"""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

Task 3
"""

import turtle as t

# Function to draw Sierpinski curve X-axis
def sierpinskyX(turtle, depth, step):
    if depth == 0:
        turtle.pencolor("blue")         # Set pen color to blue
        turtle.forward(step)
    else:
        sierpinskyY(turtle, depth - 1, step)
        turtle.left(60)
        sierpinskyX(turtle, depth - 1, step)
        turtle.left(60)
        sierpinskyY(turtle, depth - 1, step)

# Function to draw Sierpinski curve Y-axis
def sierpinskyY(turtle, depth, step):
    if depth == 0:
        turtle.pencolor("red")          # Set pen color to red
        turtle.forward(step)
    else:
        sierpinskyX(turtle, depth - 1, step)
        turtle.right(60)
        sierpinskyY(turtle, depth - 1, step)
        turtle.right(60)
        sierpinskyX(turtle, depth - 1, step)
        
# Main function to initiate Sierpinski curve drawing
def sierpinsky(turtle, depth, size=600):
    step = size / (2 ** depth)
    
    turtle.penup()
    turtle.goto(-size / 2, -size / 2.5)  # Center the drawing
    turtle.pendown()
    
    sierpinskyX(turtle, depth, step)

# Set up the turtle environment
t.setup(800, 800)
pen = t.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(4)

sierpinsky(pen, depth=5, size=700)

t.done()
