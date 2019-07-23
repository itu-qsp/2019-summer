from turtle import forward, left

angle = 170
distance = 200
nr_moves = 36
while nr_moves > 0:
    forward(distance)
    left(angle)
    nr_moves -= 1