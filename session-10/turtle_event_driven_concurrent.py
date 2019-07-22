import turtle
import platform
import threading
import subprocess
from time import sleep


turtle.setup(400, 500)
window = turtle.Screen()
window.title('Handling keypresses!')
tess = turtle.Turtle()
kind_of_speak = platform.system() == 'Darwin'

say_thread = 'I never said anything...'

# The next four functions are our "event handlers".
def go_up():
    tess.forward(30)
    window.ontimer(go_up, 160)


def turn_left():
    tess.left(45)


def turn_right():
    tess.right(45)


def quit():
    window.bye()


def say_something(msg, speak=True):
    if speak:
        cmd = f"""osascript -e 'say "{msg}"'"""
        subprocess.run(cmd, shell=True)
    else:
        for letter in msg:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.1)
        print()  # Finish with a newline


def speak():
    global say_thread

    msg = 'Move Tess the turtle!'
    if say_thread == 'I never said anything...' or not say_thread.isAlive():
        say_thread = threading.Thread(target=say_something, 
                                      args=[msg, kind_of_speak])
        say_thread.start()


# These lines 'wire up' keypresses to the handlers we've defined.
window.onkey(turn_left, 'Left')
window.onkey(turn_right, 'Right')
window.onkey(quit, 'q')
window.onkey(speak, 's')

window.ontimer(go_up, 160)


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
window.listen()
window.mainloop()