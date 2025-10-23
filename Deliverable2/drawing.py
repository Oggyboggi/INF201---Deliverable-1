"""""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

Task 1
"""""
import turtle as t

# Class pulled from lecture notebook 8
class Rectangle:
    def __init__(self, lower_left, upper_right):
        self._ll = lower_left
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]

    # Method to calculate area of the rectangle
    def area(self):
        return self._width * self._height
    
    # Method to return information about the rectangle
    def info(self):
        return f"Rectangle: lower left {self._ll}, upper right {self._ll[0] + self._width, self._ll[1] + self._height}"

    def draw(self, Turtle, scale=50):
        Turtle.penup()
        Turtle.goto(self._ll[0]*scale, self._ll[1]*scale)
        Turtle.pendown()
        for _ in range(2):
            Turtle.forward(self._width*scale)
            Turtle.left(90)
            Turtle.forward(self._height*scale)
            Turtle.left(90)

if __name__ == "__main__":
    Turtle = t.Turtle()
    rect = Rectangle((1, 2), (4, 6))
    print(rect.info())
    rect.draw(Turtle)
    t.done()
