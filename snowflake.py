import turtle

# Function pulled from "INF201_H25_D1_Intro.ipynb"
def snowflake(turtle, depth, step):
    if depth == 0:
        turtle.forward(step)          # utfør F
    else:                                 # F ->
        snowflake(turtle, depth-1, step)  #      F
        turtle.left(60)                   #        +
        snowflake(turtle, depth-1, step)  #          F
        turtle.right(60)                  #            -
        turtle.right(60)                  #              -  
        snowflake(turtle, depth-1, step)  #                F
        turtle.left(60)                   #                  +
        snowflake(turtle, depth-1, step)  #                    F

# Function to complete the snowflake by drawing three sides
def complete_snowflake(turtle, depth, size=300, linewidth=2, color='pink'):
    step = size / (3 ** depth)

    turtle.pensize(linewidth * 2)
    turtle.pencolor(color)

    turtle.penup()
    turtle.backward(size / 2)   # flytt halvparten av størrelsen til venstre
    turtle.right(90)
    turtle.forward(size / 4)    # flytt litt ned for vertikal sentrering
    turtle.goto(-size / 2, size / 4.5)
    turtle.left(90)
    turtle.pendown()

    
    for i in range(3):
        snowflake(turtle, depth, step)
        turtle.right(120)

turtle.speed(0)  # Fastest drawing speed

# Draw the snowflake
complete_snowflake(turtle=turtle, depth=3, size=300, linewidth=2, color='pink')


