from browser import document, timer, alert


class GameState:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.x_step = 5
        self.y_step = 5
        self.player_size = 20

        self.score = 0

        canvas = document['playground']
        self.ctx = canvas.getContext('2d')
        self.ctx.fillStyle = 'green'

        self.width = self.ctx.canvas.width
        self.height = self.ctx.canvas.height

        self.game_speed = 100  # ms
        # document['turnbutton'].bind("click", self.turn_it)

    def start_game(self):
        timer.set_interval(self.draw, 100)

    def restart_game(self):
        alert('Banging against the wall?')
        self.x = 10
        self.y = 10
        self.x_step = 5
        self.y_step = 5
        self.score = 0

    def clear_screen(self):
        self.ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height)

    def draw(self):
        self.clear_screen()

        self.x += self.x_step
        self.y += self.y_step

        if ((self.x < 0) or (self.x > self.width - self.player_size) or
           (self.y < 0) or (self.y > self.height - self.player_size)):
            self.restart_game()

        self.ctx.fillRect(self.x, self.y, self.player_size, self.player_size)
        self.score += 1
        document['score'].textContent = 'Your score: ' + str(score)

    def turn_it(self):
        if (self.x_step > 0) and (self.y_step > 0):
            self.y_step *= -1
        elif (self.x_step > 0) and (self.y_step < 0):
            self.x_step *= -1
        elif (self.x_step < 0) and (self.y_step < 0):
            self.y_step *= -1
        elif (self.x_step < 0) and (self.y_step > 0):
            self.x_step *= -1


clicker_game = GameState()
document['turnbutton'].bind("click", clicker_game.turn_it)

clicker_game.start_game()
