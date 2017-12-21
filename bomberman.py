from person import *

# 	Player class is inherited from person class


class Player(Person):  # inheritance from person

    def __init__(self, x, y, score, lives, timer, bombx, bomby):
        Person.__init__(self, x, y)
        self.score = score  # stores score of player
        self.lives = lives  # lives left
        self.timer = timer  # timer for bomb to blast
        self.bombx = bombx  # bomb's x_coordinate
        self.bomby = bomby  # bomb's y_coordinate

    def plant_the_bomb(self):
        return self.x_coordinate, self.y_coordinate

#	This function shows the motion off bomberman.


def bomberman_motion(move, player, A):  # move is which move the player presses
    i = player.x_coordinate
    j = player.y_coordinate
    if move == "b" and player.timer == 7:  # cant plant another bomb unless the previous bomb has exploded
        player.bombx = i
        player.bomby = j
        player.timer = 0
        # each brick the explosion destroys +20 is done to player's score.
        if A[player.bombx][player.bomby - 1] == "/":
            player.score += 20
        if A[player.bombx][player.bomby + 4] == "/":
            player.score += 20
        if A[player.bombx + 2][player.bomby] == "/":
            player.score += 20
        if A[player.bombx - 1][player.bomby] == "/":
            player.score += 20

    if move == "a":  # when the player wants to move left
        if A[i][j - 1] == "X" or A[i][j - \
            1] == "/": # obstrucion by walls or bricks
            pass
        elif A[i][j - 1] == "E":  # got killed by enemy
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.x_coordinate = 2
            player.y_coordinate = 4
            player.lives -= 1
        elif A[i][j - 1] == "o":  # if your move gave you the key
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_left()  # Exitgate opened
            for k in range(2):
                for l in range(4):
                    A[38 + k][80 + l] = "_"
        else:
            for k in range(2):  # no obstruction move free
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_left()

    if move == "d":  # when the player wants to move right
        if j < 80 and A[i][j + 4] == "X" or A[i][j + \
            4] == "/": # obstrucion by walls or bricks
            pass
        elif A[i][j + 4] == "E":  # got killed by enemy
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.x_coordinate = 2
            player.y_coordinate = 4
            player.lives -= 1
        elif A[i][j + 4] == "o":  # if your move gave you the key
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_right()  # Exitgate opened
            for k in range(2):
                for l in range(4):
                    A[38 + k][80 + l] = "_"
        else:
            for k in range(2):  # no obstruction move free
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_right()

    if move == "w":  # when the player wants to move up
        if A[i - 1][j] == "X" or A[i -
                                   1][j] == "/":  # obstrucion by walls or bricks
            pass
        elif A[i - 1][j] == "E":  # got killed by enemy
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.x_coordinate = 2
            player.y_coordinate = 4
            player.lives -= 1
        elif A[i - 2][j] == "o":  # if your move gave you the key
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_up()  # Exitgate opened
            for k in range(2):
                for l in range(4):
                    A[38 + k][80 + l] = "_"
        else:
            for k in range(2):  # no obstruction move free
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_up()

    if move == "s":  # when the player wants to move down
        if A[i + 2][j] == "X" or A[i +
                                   2][j] == "/":  # obstrucion by walls or bricks
            pass
        elif A[i + 2][j] == "E":  # got killed by enemy
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.x_coordinate = 2
            player.y_coordinate = 4
            player.lives -= 1
        elif A[i + 2][j] == "o":  # if your move gave you the key
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_down()  # Exitgate opened
            for k in range(2):
                for l in range(4):
                    A[38 + k][80 + l] = "_"
        else:
            for k in range(2):  # no obstruction move free
                for l in range(4):
                    A[i + k][j + l] = " "
            player.move_down()
