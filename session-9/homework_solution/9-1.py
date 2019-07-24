class Mario():
    def __init__(self, star):
        self.mario_x = 0
        self.mario_y = 0

        self.star_x = star[0]
        self.star_y = star[1]

        self.points = 0

    def check_star(self):
        if (self.mario_x == self.star_x and self.mario_y == self.star_y):
            self.points += 1

    def down(self):
        self.mario_y -= 1
        self.check_star()

    def left(self):
        self.mario_x -= 1
        self.check_star()

    def up(self):
        self.mario_y += 1
        self.check_star()

    def right(self):
        self.mario_x += 1
        self.check_star()


m = Mario((0, 2))

print(m.points)
m.up()
m.up()
print(m.points)
