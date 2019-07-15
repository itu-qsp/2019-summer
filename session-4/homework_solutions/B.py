#B
from turtle import forward, right

#get height input
#get width input

#loop twice:
    #draw 1 line (height)
    #turn 90 degrees
    #draw another line (width)
    #turn 90 degrees

making_rectangle = True
while making_rectangle:
    try:
        height = int(input("Height: "))
        width = int(input("Width: "))

        count = 2
        while count > 0:
            forward(height)
            right(90)
            forward(width)
            right(90)
            count -= 1
        """
        solutiution 2.
        instead of while, use a for loop:

        for i in range(2):
            forward(height)
            right(90)
            forward(width)
            right(90)
        """

        making_rectangle = False

    except:
        print("Please type a number!!!!")
