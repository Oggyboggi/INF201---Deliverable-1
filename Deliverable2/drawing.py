"""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

INF201 - Deliverable 2
"""
import turtle as t
import math

"""
Rectangle class template is pulled from Lecture notebook 8.
Down under is the modified and complete version
"""

class Rectangle:
    def __init__(self, lower_left, upper_right, color="black", linewidth=1):
        self._ll = lower_left
        self._ur = upper_right
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]
        self._color = color
        self._linewidth = linewidth
        
    # Method to define area of rectangle
    def area(self):
        return self._width * self._height
    
    # Method to print info about rectangle
    def info(self):
        print(f"Rectangle: lower left {self._ll}, upper right {self._ur}")
        
    # Method to draw rectangle using turtle
    def draw(self, turtle_obj, scale=50):
        turtle_obj.penup()
        turtle_obj.goto(self._ll[0] * scale, self._ll[1] * scale)
        turtle_obj.pendown()
        turtle_obj.pencolor(self._color)
        turtle_obj.pensize(self._linewidth)

        for _ in range(2):
            turtle_obj.forward(self._width * scale)
            turtle_obj.left(90)
            turtle_obj.forward(self._height * scale)
            turtle_obj.left(90)


# Class for Triangle
class Triangle:
    def __init__(self, p1, p2, p3, color="red", linewidth=1):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._color = color
        self._linewidth = linewidth
        
    # Method to calculate area of triangle using determinant formula
    def area(self):
        x1, y1 = self._p1
        x2, y2 = self._p2
        x3, y3 = self._p3
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    # Method to print info about triangle
    def info(self):
        print(f"Triangle: points {self._p1}, {self._p2}, {self._p3}, "
              f"color {self._color}, linewidth {self._linewidth}, area {self.area()}")
        
    # Method to draw triangle using turtle
    def draw(self, turtle_obj, scale=50):
        turtle_obj.penup()
        turtle_obj.pencolor(self._color)
        turtle_obj.pensize(self._linewidth)

        p1s = (self._p1[0] * scale, self._p1[1] * scale)
        p2s = (self._p2[0] * scale, self._p2[1] * scale)
        p3s = (self._p3[0] * scale, self._p3[1] * scale)

        turtle_obj.goto(*p1s); turtle_obj.pendown()
        turtle_obj.goto(*p2s); turtle_obj.goto(*p3s); turtle_obj.goto(*p1s)
        turtle_obj.penup()

# Class for Circle
class Circle:
    # Initialize circle with center, radius, color, and linewidth
    def __init__(self, center, radius, color="blue", linewidth=1):
        self._center = center
        self._radius = radius
        self._color = color
        self._linewidth = linewidth
        
    # Method to define area of circle
    def info(self):
        print(f"Circle: center {self._center}, radius {self._radius}, "
              f"color {self._color}, linewidth {self._linewidth}")
        
    # Method to draw circle using turtle
    def draw(self, turtle_obj, scale=50, sides=60):
        cx, cy = self._center
        r = self._radius
        
        # Calculate starting point on the circumference
        start = ((cx + r) * scale, cy * scale)

        turtle_obj.penup()
        turtle_obj.pencolor(self._color)
        turtle_obj.pensize(self._linewidth)
        turtle_obj.goto(*start)
        turtle_obj.setheading(0)
        turtle_obj.pendown()

        side_len = (2 * math.pi * r / sides) * scale
        turn = 360 / sides
        
        # Draw the approximated circle
        for _ in range(sides):
            turtle_obj.forward(side_len)
            turtle_obj.left(turn)
        turtle_obj.penup()

# Main program to test the classes
if __name__ == "__main__":
    Turtle = t.Turtle()
    Turtle.speed(0)
    Turtle.hideturtle()

    # Test Rectangles
    print("--- Rectangles ---")
    rects = [
        Rectangle((-5, -2), (-2, 2), color="black", linewidth=3),
        Rectangle((-0, -1), (3, 1), color="gray", linewidth=2),
        Rectangle((4, -0.5), (6.5, 1.5), color="purple", linewidth=2),
    ]
    
    for r in rects:
        r.info()
        r.draw(Turtle, scale=50)

    print()
    # Test Triangles
    print("--- Triangles ---")
    triangles = [
        Triangle((0, -4), (2, -4), (1, -2), color="red", linewidth=2),
        Triangle((-3, -5), (-1, -5), (-2, -3), color="green", linewidth=3),
    ]
    
    for tri in triangles:
        tri.info()
        tri.draw(Turtle, scale=50)
    print()
    # Test Circles
    print("--- Circles ---")
    circles = [
        Circle((5, 3), 1, color="blue", linewidth=2),
        Circle((-4, 3), 0.5, color="orange", linewidth=3),
    ]
    for c in circles:
        c.info()
        c.draw(Turtle, scale=50, sides=60)

    t.done()
