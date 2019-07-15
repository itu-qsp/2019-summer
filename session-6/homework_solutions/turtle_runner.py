import sys
from turtle import Turtle, done


def do_line(turtle, command, value):
    if command == "Walk":
        turtle.forward(value)
    else:
        turtle.right(value)


def main(path_to_file):
    turtle = Turtle(shape="turtle")
    with open(path_to_file,"r") as f:
        lines = f.read().split("\n")
    for line in lines:
        command, value = line.split()
        do_line(turtle, command,int(value))

if __name__ == '__main__':
    main(sys.argv[1])
    done()