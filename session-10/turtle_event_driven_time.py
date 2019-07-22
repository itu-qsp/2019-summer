import sys
import turtle


turtle.setup(400, 500)
window = turtle.Screen()
window.title('Handling keypresses!')
tess = turtle.Turtle()


def go_up():
    tess.forward(30)
    window.ontimer(go_up, 160)


def turn_left():
    tess.left(45)


def turn_right():
    tess.right(45)


def quit():
    window.bye()
    sys.exit() 


# These lines 'wire up' keypresses to the handlers we've defined.
window.onkey(turn_left, 'Left')
window.onkey(turn_right, 'Right')
window.onkey(quit, 'q')

window.ontimer(go_up, 160)

window.listen()
window.mainloop()
