from turtle import Turtle, done


class GeometryTurtle(Turtle):
    # TODO: Implement me!!!
    pass


def main():
    my_turtle = GeometryTurtle()
    my_turtle.make_square(50)

    my_turtle.penup()
    my_turtle.forward(70)
    my_turtle.pendown()

    for i in range(6):
        my_turtle.right(60)
        my_turtle.make_square(30)

    my_turtle.penup()
    my_turtle.forward(70)
    my_turtle.pendown()

    my_turtle.make_rectangle(50, 20)

    my_turtle.penup()
    my_turtle.forward(70)
    my_turtle.pendown()

    my_turtle.make_triangle(50)

    my_turtle.penup()
    my_turtle.forward(70)
    my_turtle.pendown()

    my_turtle.make_star(49)

    # The call to the function `done` from the `turtle` module means that you
    # Have to close the window manually
    done()


if __name__ == '__main__':
    main()
