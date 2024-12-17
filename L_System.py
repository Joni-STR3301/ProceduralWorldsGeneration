import turtle

def l_system(axiom, rules, iterations):
    for _ in range(iterations):
        new_axiom = ''.join(rules.get(ch, ch) for ch in axiom)
        axiom = new_axiom
    return axiom

def draw_l_system(axiom, angle, length):
    try:
        stack = []
        for command in axiom:
            if command == 'F':
                turtle.forward(length)
            elif command == '+':
                turtle.right(angle)
            elif command == '-':
                turtle.left(angle)
            elif command == '[':
                stack.append((turtle.position(), turtle.heading()))
            elif command == ']':
                position, heading = stack.pop()
                turtle.penup()
                turtle.goto(position)
                turtle.setheading(heading)
                turtle.pendown()
    except BaseException:
        None

def run():
    rules = {'F': 'FF+[+F-F-F]-[-F+F+F]'}
    axiom = 'F'
    iterations = 4
    turtle.speed(0)
    turtle.left(90)

    axiom_result = l_system(axiom, rules, iterations)
    draw_l_system(axiom_result, 25, 5)
    turtle.done()


# defolt - FF+[+F-F-F]-[-F+F+F]
# FF[+F][--FF][-F+F]