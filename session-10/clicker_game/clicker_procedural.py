from browser import document, timer, alert


canvas = document['playground']
ctx = canvas.getContext('2d')
ctx.fillStyle = 'green'

x = 10
y = 10
x_step = 5
y_step = 5
player_size = 20

score = 0


def clear_screen():
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height)


def draw():
    global x
    global y
    global x_step
    global y_step
    global score

    clear_screen()

    x += x_step
    y += y_step

    if ((x < 0) or (x > ctx.canvas.width - player_size) or (y < 0) or
       (y > ctx.canvas.height - player_size)):
        alert('Banging against the wall?')
        x = 10
        y = 10
        x_step = 5
        y_step = 5
        score = 0

    ctx.fillRect(x, y, player_size, player_size)
    score += 1
    document['score'].textContent = 'Your score: ' + str(score)


def turn_it():
    global x_step
    global y_step

    if (x_step > 0) and (y_step > 0):
        y_step *= -1
    elif (x_step > 0) and (y_step < 0):
        x_step *= -1
    elif (x_step < 0) and (y_step < 0):
        y_step *= -1
    elif (x_step < 0) and (y_step > 0):
        x_step *= -1


timer.set_interval(draw, 100)

document['turnbutton'].bind('click', turn_it)
