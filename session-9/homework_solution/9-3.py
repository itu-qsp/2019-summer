class Mario():
    def __init__(self):
        self.mario_x = 0
        self.mario_y = 0
        self.points = 0
        self.is_alive = True

        with open('../9/field-1.txt') as f:
            self.load_level(f.readlines())

    def check_alive(self):
        if self.level[self.mario_y][self.mario_x] == '#':
            self.is_alive = False
        return self.is_alive

    def check_star(self):
        if (self.mario_x == self.star_x and self.mario_y == self.star_y):
            self.points += 1

    def down(self):
        if self.check_alive():
            self.mario_y -= 1
            self.check_star()

    def left(self):
        if self.check_alive():
            self.mario_x -= 1
            self.check_star()

    def load_level(self, level):
        # Flip the y-coordinate
        self.level = level[::-1]
        for y_id, line in enumerate(self.level):
            for x_id, character in enumerate(line):
                if character == '*':
                    self.star_x = x_id
                    self.star_y = y_id

    def up(self):
        if self.check_alive():
            self.mario_y += 1
            self.check_star()

    def right(self):
        if self.check_alive():
            self.mario_x += 1
            self.check_star()

    def simulate(self, moves):
        mario = Mario()

        for move in moves:
            if move == 'U':
                mario.up()
            elif move == 'L':
                mario.left()
            elif move == 'D':
                mario.down()
            elif move == 'R':
                mario.right()

            if not mario.is_alive:
                break

        if not mario.is_alive:
            return 'Mario died!'
        else:
            return mario.points


for move in [1, 2, 3, 4]:
    with open('../9/moves-{}.txt'.format(move)) as f:
        moves = f.readline()
        print('Move {}: {}'.format(move, Mario().simulate(moves)))
