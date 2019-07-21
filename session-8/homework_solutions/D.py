#D:

import turtle
from timeit import default_timer

start = default_timer()

turtle = turtle.Turtle()
n = 32
moves = [100] * n
for move in moves:
    turtle.forward(move)
    turtle.left(45)

end = default_timer()

print(end-start)

#If I double the runtime to 16, the octagon gets drawn twice, so it takes twice as long. (n = 8 -> 1.785, n = 16 --> 3.422)
#Same goes for doubling again, so with n = 32 it would take 4x as much time. (n = 32 -> 6.851)
#O(n), the runtime is linear.