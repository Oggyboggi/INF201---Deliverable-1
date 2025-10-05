import turtle

# Function pulled from "INF201_H25_D1_Intro.ipynb"
def snowflake(turtle, depth):
    if depth == 0:
        turtle.forward(10)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1)  #                    F

# Function to complete the snowflake by drawing three sides
def complete_snowflake(turtle, depth):
    for i in range(3):
        snowflake(turtle, 3)
        turtle.right(120)

turtle.speed(0)  # Fastest drawing speed

# Draw the snowflake
complete_snowflake(turtle=turtle, depth=3)
