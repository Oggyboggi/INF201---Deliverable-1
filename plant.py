import turtle as tt

def generate(axiom: str, rules: dict[str, str], iterations: int) -> str:
    s = axiom
    for _ in range(iterations):
        s = ''.join(rules.get(ch, ch) for ch in s)
    return s

def draw(sentence: str, angle: float = 25.0, step: float = 5.0,
         linewidth: int = 2, color: str = "green") -> None:
    screen = tt.Screen()
    t = tt.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(linewidth)
    t.pencolor(color)

    # Start nederst i vinduet, pekende opp
    screen.update()
    t.penup()
    t.goto(0, -screen.window_height() // 2 + 40)
    t.setheading(90)
    t.pendown()

    stack: list[tuple[tuple[float, float], float]] = []

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
        # 'X' og andre tegn: ingen tegning

    screen.mainloop()

def plant(iterations: int = 5, angle: float = 25.0,
          size: float = 300.0, linewidth: int = 2, color: str = "green") -> None:
    rules = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
    }
    axiom = "X"
    sentence = generate(axiom, rules, iterations)

    # Grovt skaleringsvalg: segmentlengde minker eksponentielt med iterasjoner
    step = size / (2 ** iterations)

    draw(sentence, angle=angle, step=step, linewidth=linewidth, color=color)

if __name__ == "__main__":
    # Justér gjerne parametrene under
    plant(iterations=5, angle=25, size=300, linewidth=2, color="forest green")