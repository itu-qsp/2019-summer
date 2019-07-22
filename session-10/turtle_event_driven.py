import sys
import turtle


turtle.setup(400, 500)
window = turtle.Screen()
window.title('Handling keypresses!')
tess = turtle.Turtle()

say_thread = 'I never said anything...'

# The next four functions are our 'event handlers'.
def go_up():
    tess.forward(30)


def turn_left():
    tess.left(45)


def turn_right():
    tess.right(45)


def quit():
    window.bye()  # Close down the turtle window


# These lines 'wire up' keypresses to the handlers we've defined.
window.onkey(go_up, 'Up')
window.onkey(turn_left, 'Left')
window.onkey(turn_right, 'Right')
window.onkey(quit, 'q')


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
window.listen()
window.mainloop()