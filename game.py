from bomberman import *
from get_input import *
from enemy import *
from wall import *
import signal
import copy
import sys
import time
import random
import math
from termcolor import colored
import os

'''
A is the 2-D array for the game that holds which game character is stored on a particular position on board.
enemy is an array of enemies in the game with max enemies to be 10
player is the player playing game starting at 2,4 in the board.
'''

A = [[" " for i in range(84)] for j in range(42)]
enemy = [" " for i in range(10)]
player = Player(2, 4, 0, 3, 10, 0, 0)
key_appeared = 0

createwall(A)
insert_bricks(A)
player.timer = 7
create_enemies(A, enemy)


def printstatus():  # this function updates the board i.e A 2-d array
    print("PLAYER :- player_1")
    i = player.x_coordinate
    # print first the score and lives left of the player.
    j = player.y_coordinate
    print("PLAYER => player01  SCORE => " + str(player.score) +
          "  LIVES LEFT => " + str(player.lives) + "\n\n")
    for k in range(2):  # updating the position of the bomberman on the board
        for l in range(4):
            A[i + k][j + l] = "B"

    # playertimer is used to recognize and make sure that another bomb is not
    # planted before the first bomb completely explodes

    if player.timer < 7:  # bonus question i.e to countdown before the bomb explodes
        if(player.timer < 4):
            for k in range(2):
                for l in range(4):
                    A[player.bombx + k][player.bomby + l] = 3 - player.timer
        player.timer += 1

    if player.timer == 5:
        for en_i in range(1, 6):
            if enemy[en_i].alive == 1:
                flag = 0
                if enemy[en_i].x_coordinate == player.bombx and enemy[en_i].y_coordinate == player.bomby - 4:
                    flag += 1
                elif enemy[en_i].x_coordinate == player.bombx + 2 and enemy[en_i].y_coordinate == player.bomby:
                    flag += 1
                elif enemy[en_i].x_coordinate == player.bombx and enemy[en_i].y_coordinate == player.bomby + 4:
                    flag += 1
                elif enemy[en_i].x_coordinate == player.bombx - 2 and enemy[en_i].y_coordinate == player.bomby:
                    flag += 1
                if flag == 1:
                    player.score += 100
                    enemy[en_i].alive = 0
                    for k in range(2):
                        for l in range(4):
                            A[enemy[en_i].x_coordinate +
                                k][enemy[en_i].y_coordinate + l] = " "
        if (
            (
                player.x_coordinate == player.bombx) and (
                player.y_coordinate == player.bomby)) or (
                (player.x_coordinate == player.bombx) and (
                    player.y_coordinate == player.bomby -
                    4)) or (
                        (player.x_coordinate == player.bombx) and (
                            player.y_coordinate == player.bomby +
                            4)) or (
                                (player.x_coordinate == player.bombx -
                                 2) and (
                                    player.y_coordinate == player.bomby)) or (
                                        (player.x_coordinate == player.bombx +
                                         2) and (
                                            player.y_coordinate == player.bomby)):
            player.x_coordinate = 2
            player.y_coordinate = 4
            player.lives -= 1
            for k in range(2):
                for l in range(4):
                    A[i + k][j + l] = " "

        #	implementing the explosion. 'e' color magenta.
        #	at 5 positions the explosion is detected.

        for ex_x in range(1, 3):  # explosion in upward direction
            for ex_y in range(4):
                if (player.bombx - ex_x > 1) and (player.bomby + ex_y < 80):
                    if A[player.bombx -
                         ex_x][player.bomby +
                               ex_y] == " " or A[player.bombx -
                                                 ex_x][player.bomby +
                                                       ex_y] == "/" or A[player.bombx -
                                                                         ex_x][player.bomby +
                                                                               ex_y] == "B":
                        A[player.bombx - ex_x][player.bomby + ex_y] = "e"

        for ex_x in range(2, 4):  # explosion in downward direction
            for ex_y in range(4):
                if (player.bombx + ex_x < 40) and (player.bomby + ex_y < 80):
                    if A[player.bombx +
                         ex_x][player.bomby +
                               ex_y] == " " or A[player.bombx +
                                                 ex_x][player.bomby +
                                                       ex_y] == "/" or A[player.bombx +
                                                                         ex_x][player.bomby +
                                                                               ex_y] == "B":
                        A[player.bombx + ex_x][player.bomby + ex_y] = "e"

        for ex_x in range(2):  # explosion in left direction
            for ex_y in range(1, 5):
                if (player.bombx + ex_x < 40) and (player.bomby - ex_y > 4):
                    if A[player.bombx +
                         ex_x][player.bomby -
                               ex_y] == " " or A[player.bombx +
                                                 ex_x][player.bomby -
                                                       ex_y] == "/" or A[player.bombx +
                                                                         ex_x][player.bomby -
                                                                               ex_y] == "B":
                        A[player.bombx + ex_x][player.bomby - ex_y] = "e"

        for ex_x in range(2):  # explosion in right direction
            for ex_y in range(4, 8):
                if (player.bombx + ex_x < 40) and (player.bomby + ex_y < 80):
                    if A[player.bombx +
                         ex_x][player.bomby +
                               ex_y] == " " or A[player.bombx +
                                                 ex_x][player.bomby +
                                                       ex_y] == "/" or A[player.bombx +
                                                                         ex_x][player.bomby +
                                                                               ex_y] == "B":
                        A[player.bombx + ex_x][player.bomby + ex_y] = "e"

        for ex_x in range(2):  # explosion in the original bomb planted place.
            for ex_y in range(4):
                A[player.bombx + ex_x][player.bomby + ex_y] = "e"

    #	disappearing explosion trail after the explosion.

    if player.timer == 6:
        for ex_x in range(1, 3):
            for ex_y in range(4):
                if (player.bombx - ex_x > 1) and (player.bomby + ex_y < 80):
                    if A[player.bombx - ex_x][player.bomby + ex_y] == "e":
                        A[player.bombx - ex_x][player.bomby + ex_y] = " "
        for ex_x in range(2, 4):
            for ex_y in range(4):
                if (player.bombx + ex_x < 40) and (player.bomby + ex_y < 80):
                    if A[player.bombx + ex_x][player.bomby + ex_y] == "e":
                        A[player.bombx + ex_x][player.bomby + ex_y] = " "
        for ex_x in range(2):
            for ex_y in range(1, 5):
                if (player.bombx + ex_x < 40) and (player.bomby - ex_y > 4):
                    if A[player.bombx + ex_x][player.bomby - ex_y] == "e":
                        A[player.bombx + ex_x][player.bomby - ex_y] = " "
        for ex_x in range(2):
            for ex_y in range(4, 8):
                if (player.bombx + ex_x < 40) and (player.bomby + ex_y < 80):
                    if A[player.bombx + ex_x][player.bomby + ex_y] == "e":
                        A[player.bombx + ex_x][player.bomby + ex_y] = " "
        for ex_x in range(2):
            for ex_y in range(4):
                A[player.bombx + ex_x][player.bomby + ex_y] = " "

    color_printing()


def color_printing():  # package termcolor is to be installed then printstatus calls this function where each character in board is
    for i in range(42):  # is printed with some specific color.
        for j in range(84):
            if A[i][j] == "X":
                print colored(A[i][j], "cyan"),
            elif A[i][j] == "B":
                print colored(A[i][j], "green"),
            elif A[i][j] == "E":
                print colored(A[i][j], "red"),
            elif A[i][j] == "/":
                print colored(A[i][j], "yellow"),
            elif A[i][j] == "e":
                print colored(A[i][j], "magenta"),
            else:
                print A[i][j],
        print "\0"


while (1):  # infinite loop unless the player dies or he wins the game.
    take_or_not = 1
    i = player.x_coordinate
    j = player.y_coordinate
    take = 1
    enemy_left = 0

    # calling the motion of enemies to update the  board.
    enemy_left = enemy_motion(A, enemy, player)

    # if all the enemies are dead, key appears at random position on the board
    if enemy_left == 0 and key_appeared == 0:
        en_x = 2 * random.randint(2, 19)
        en_y = 4 * random.randint(3, 19)
        while((A[en_x][en_y] != " ")):
            en_x = 2 * random.randint(2, 19)
            en_y = 4 * random.randint(3, 19)

        for l in range(
                4):  # updating the board with the key at random position
            A[en_x][en_y + l] = "o"
        A[en_x + 1][en_y + 2] = "o"
        A[en_x + 1][en_y + 3] = "o"
        key_appeared = 1

    if(take == 1) and (j != 80):  # if you are already at the exit gate then no input is to be taken
        move = input_to()  # move holds the keystroke value
        if move != "q":
            # changing the position of the bomberman according to the input
            bomberman_motion(move, player, A)
        else:
            break

    if player.lives <= 0:  # if the bomberman is dead then end the game and print the score
        print("\n\n\n\nGAME OVER")
        print("YOUR SCORE IS  ===>>>  " + str(player.score))
        break
    if (i == 38) and (
            j == 80):  # if exit gate is reached then the game is won so print the score and the lives left
        print("\n\n\n\nYOU HAVE WON THIS GAME BUDDY")
        print("NUMBER OF LIVES LEFT IS  ===>>>  " + str(player.lives))
        print("YOUR SCORE IS  ===>>>  " + str(player.score))
        break

    # for clear printing of the board so that it appears clean
    os.system('clear')

    printstatus()  # print the board.
