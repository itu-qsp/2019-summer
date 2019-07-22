import sys
import turtle


turtle.setup(400, 500)
window = turtle.Screen()
window.title('Handling keypresses!')
tess = turtle.Turtle()


def move():
    tess.forward(30)

def turn_left():
    tess.left(45)

def turn_right():
    tess.right(45)

def quit():
    window.bye()
    sys.exit()


while True:
    command = input('What shall I do? ')
    print('Received command: ' + command)
    if command == 'm':
        move()
    elif command == 'l':
        turn_left()
    elif command == 'r':
        turn_right()
    elif command == 'q':
        quit()
    else:
        print('Valid commands are `m`, `l`, `r`, `q`...')