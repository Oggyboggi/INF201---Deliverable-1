import turtle as t

# Function to draw Sierpinski curve X-axis
def sierpinskyX(turtle, depth, length):
    turtle.pencolor("blue") # Set pen color to blue
    if depth == 0:
        turtle.forward(length)
    else:
        sierpinskyY(turtle, depth - 1, length)
        turtle.left(60)
        turtle.forward(length)
        sierpinskyX(turtle, depth - 1, length)
        turtle.left(60)
        turtle.forward(length)
        sierpinskyY(turtle, depth - 1, length)

# Function to draw Sierpinski curve Y-axis
def sierpinskyY(turtle, depth, length):
    turtle.pencolor("red") # Set pen color to red
    if depth == 0:
        turtle.forward(length)
    else:
        sierpinskyX(turtle, depth - 1, length)
        turtle.right(60)
        turtle.forward(length)
        sierpinskyY(turtle, depth - 1, length)
        turtle.right(60)
        turtle.forward(length)
        sierpinskyX(turtle, depth - 1, length)
        
# Main function to initiate Sierpinski curve drawing
def sierpinsky(turtle, depth):
    sierpinskyX(turtle, depth, 10)

# Set up the turtle environment
t.setup(800, 800)
pen = t.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200, 150)
pen.pendown()

sierpinsky(pen, 4)
t.done()
