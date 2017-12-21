from person import *
import random

# 	Enemy class is inherited from person class


class Enemy(Person):  # inheritance from person

    def __init__(self, x, y, alive):
        Person.__init__(self, x, y)
        self.alive = alive  # enemy is alive or not

#	creating enemies at random positions on board.


def create_enemies(A, enemy):
    i = 0
    j = 0
    for i in range(1, 4):
        # enemies created a bit far from player's first point of creation
        en_x = 2 * random.randint(2, 19)
        en_y = 4 * random.randint(3, 19)
        while((A[en_x][en_y] != " ")):
            en_x = 2 * random.randint(2, 19)
            en_y = 4 * random.randint(3, 19)
            for j in range(
                    1, i):  # no two enemies should have the same position .
                if en_x == enemy[j].x_coordinate and en_y == enemy[j].y_coordinate:
                    break
            if j == i:
                break

        enemy[i] = Enemy(en_x, en_y, 1)  # enemies are represented by E
        for k in range(2):
            for l in range(4):
                A[en_x + k][en_y + l] = "E"

    for i in range(4, 6):  # two enemies for sure to safeguard the exitgate.
        en_x = 38
        en_y = 4 * random.randint(1, 19)
        while A[en_x][en_y] != " ":
            en_y = 4 * random.randint(1, 19)
        enemy[i] = Enemy(en_x, en_y, 1)
        for k in range(2):
            for l in range(4):
                A[en_x + k][en_y + l] = "E"

# this function decides the future position of each enemy from its current
# position.


def enemy_motion(A, enemy, player):
    enemy_left = 0
    for en_i in range(1, 6):
        # if the enemy is alive then only the point of moving arises.
        if enemy[en_i].alive == 1:
            enemy_left = 1
            en_j = enemy[en_i].x_coordinate
            en_k = enemy[en_i].y_coordinate
            # if it sees the player next to it then kill the player.
            if A[en_j][en_k - 1] == "B" and en_k > 4:
                for k in range(2):
                    for l in range(4):
                        A[en_j + k][en_k + l] = " "
                player.x_coordinate = 2
                player.y_coordinate = 4
                player.lives -= 1  # player lives go down by one.
                take = 0 	# to say that bomberman is dead so taking any inputs.
                enemy[en_i].move_left()

            elif A[en_j][en_k + 4] == "B":
                for k in range(2):
                    for l in range(4):
                        A[en_j + k][en_k + l] = " "
                player.x_coordinate = 2
                player.y_coordinate = 4
                player.lives -= 1
                take = 0 	# to say that bomberman is dead so taking any inputs.
                enemy[en_i].move_right()

            elif A[en_j - 1][en_k] == "B" and en_j > 4:
                for k in range(2):
                    for l in range(4):
                        A[en_j + k][en_k + l] = " "
                player.x_coordinate = 2
                player.y_coordinate = 4
                player.lives -= 1
                take = 0  # to say that bomberman is dead so taking any inputs.
                enemy[en_i].move_up()

            elif A[en_j + 2][en_k] == "B":
                for k in range(2):
                    for l in range(4):
                        A[en_j + k][en_k + l] = " "
                player.x_coordinate = 2
                player.y_coordinate = 4
                player.lives -= 1
                take = 0  # to say that bomberman is dead so taking any inputs.
                enemy[en_i].move_down()

            else:
                # if no player around then go randomly in the direction of
                # space availble.
                rand = random.randint(1, 4)

                if rand == 1 and A[en_j][en_k - 1] == " " and en_k > 4:
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_left()

                elif rand == 2 and A[en_j][en_k + 4] == " ":
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_right()

                elif rand == 3 and A[en_j - 1][en_k] == " " and en_j > 8:
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_up()

                elif rand == 4 and A[en_j + 2][en_k] == " ":
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_down()

                elif A[en_j][en_k - 1] == " " and en_k > 4:
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_left()

                elif A[en_j][en_k + 4] == " ":
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_right()

                elif A[en_j - 1][en_k] == " " and en_j > 8:
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_up()

                elif A[en_j + 2][en_k] == " ":
                    for k in range(2):
                        for l in range(4):
                            A[en_j + k][en_k + l] = " "
                    enemy[en_i].move_down()

            en_j = enemy[en_i].x_coordinate		# updating the position of enemies
            en_k = enemy[en_i].y_coordinate
            for k in range(2):
                for l in range(4):
                    A[en_j + k][en_k + l] = "E"

    return enemy_left  # to know how many enemies are left so as to get the key to exitgate
