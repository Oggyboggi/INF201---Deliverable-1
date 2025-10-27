
"""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

Task 1 + start Task 2
"""
import turtle as t

# Rectangle-klassen bygger på eksempelet fra forelesning 8.
# Kilde: Forelesningsnotat (Lecture 8).


class Rectangle:
    def __init__(self, lower_left, upper_right):
        self._ll = lower_left
        self._ur = upper_right
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]

    def area(self):
        return self._width * self._height

    def info(self):
        print(f"Rectangle: lower left {self._ll}, upper right {self._ur}")

    def draw(self, turtle_obj, scale=50):
        turtle_obj.penup()
        turtle_obj.goto(self._ll[0] * scale, self._ll[1] * scale)
        turtle_obj.pendown()
        turtle_obj.pensize(3)

        for _ in range(2):
            turtle_obj.forward(self._width * scale)
            turtle_obj.left(90)
            turtle_obj.forward(self._height * scale)
            turtle_obj.left(90)


# Oppgave 3: Partially done, to be completed by partner
class Triangle:
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        # TODO: add color and linewidth as keyword arguments
        # TODO: implement info() that prints points, color, linewidth
        # TODO: implement draw() using turtle


class Circle:
    def __init__(self, center, radius):
        self._center = center
        self._radius = radius
        # TODO: add color and linewidth as keyword arguments
        # TODO: implement info()
        # TODO: draw as many-sided polygon with turtle


if __name__ == "__main__":
    Turtle = t.Turtle()
    Turtle.speed(0)

    # Task 1 & Task 2
    rects = [
        Rectangle((-1.5, -2), (1.5, 2)),
        Rectangle((-4, -1), (-1, 1)),
        Rectangle((2, -0.5), (4.5, 1.5))
    ]

    print("== Rectangles ==")
    for r in rects:
        r.info()
        r.draw(Turtle, scale=50)

    # Task 3 will be completed later
    # TODO: create list of Triangle and Circle instances
    # TODO: call info() and draw() for each

    t.done()
