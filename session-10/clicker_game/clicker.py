from browser import document, timer, alert


class GameState:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.x_step = 5
        self.y_step = 5

        self.score = 0


PLAYER_SIZE = 20

canvas = document['playground']
ctx = canvas.getContext('2d')
ctx.fillStyle = 'green'

clicker_state = GameState()


def restart_game():
    alert('Banging against the wall?')
    clicker_state.x = clicker_state.y = 10
    clicker_state.x_step = clicker_state.y_step = 5
    clicker_state.score = 0


def clear_screen():
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height)


def draw():
    clear_screen()

    clicker_state.x += clicker_state.x_step
    clicker_state.y += clicker_state.y_step

    if ((clicker_state.x < 0) or
       (clicker_state.x > ctx.canvas.width - PLAYER_SIZE) or
       (clicker_state.y < 0) or
       (clicker_state.y > ctx.canvas.height - PLAYER_SIZE)):
        restart_game()

    ctx.fillRect(clicker_state.x, clicker_state.y, PLAYER_SIZE, PLAYER_SIZE)
    clicker_state.score += 1
    document['score'].textContent = 'Your score: ' + str(clicker_state.score)


def turn_it():
    going_right = (clicker_state.x_step > 0)
    going_left = (clicker_state.x_step < 0)
    going_down = (clicker_state.y_step > 0)
    going_up = (clicker_state.y_step < 0)
    if (going_right and going_down) or (going_left and going_up):
        clicker_state.y_step *= -1
    elif (going_right and going_up) or (going_left and going_down):
        clicker_state.x_step *= -1

    clicker_state.score -= 20


timer.set_interval(draw, 50)

document['turnbutton'].bind('click', turn_it)
