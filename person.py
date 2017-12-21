#	main class from which Player and Enemy are inherited


class Person():

    def __init__(self, x, y):
        self.x_coordinate = x  # initial x coordinate
        self.y_coordinate = y  # initial y coordinate

    def move_right(self):  # method to move right
        self.y_coordinate += 4  # increment y position by 4

    def move_left(self):  # method to move left
        self.y_coordinate -= 4  # decrement y position by 2

    def move_up(self):  # method to move up
        self.x_coordinate -= 2  # decrement x position by 2

    def move_down(self):  # method to move down
        self.x_coordinate += 2  # increment x position by 2
