"""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

Task 4
"""
import turtle as tt

# L-system generator
def generate(axiom: str, rules: dict[str, str], iterations: int) -> str:
    s = axiom
    for _ in range(iterations):
        s = ''.join(rules.get(ch, ch) for ch in s)
    return s

# drawing function using turtle graphics
def draw(sentence: str, angle: float = 25.0, step: float = 5.0,
         linewidth: int = 2, color: str = "green") -> None:
    screen = tt.Screen()
    t = tt.Turtle()
    t.hideturtle()
    t.speed(5)
    t.pensize(linewidth)
    t.pencolor(color)
    screen.update()
    t.penup()
    t.goto(0, -screen.window_height() // 2 + 40)
    t.setheading(90)
    t.pendown()
    
    stack: list[tuple[tuple[float, float], float]] = []

    # L-system drawing logic
    for ch in sentence:
        if ch == 'F':
            t.forward(step)
        elif ch == '+':
            t.right(angle)
        elif ch == '-':
            t.left(angle)
        elif ch == '[':
            stack.append((t.position(), t.heading()))
        elif ch == ']':
            if stack:
                pos, head = stack.pop()
                t.penup()
                t.goto(pos)
                t.setheading(head)
                t.pendown()
                
    screen.mainloop()

# Main function to generate and draw the plant
def plant(iterations: int = 5, angle: float = 25.0,
          size: float = 300.0, linewidth: int = 3, color: str = "green") -> None:
    rules = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
    }
    axiom = "X"
    sentence = generate(axiom, rules, iterations)

    # initial step size adjusted for iterations
    step = size / (2 ** iterations)
    draw(sentence, angle=angle, step=step, linewidth=linewidth, color=color)
    
#Draw the plant if this file is run as a script
if __name__ == "__main__":

    plant()
