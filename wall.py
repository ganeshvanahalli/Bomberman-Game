import random

#	wall is represented as X in the 2-D array A[][]


def createwall(A):  # the wall is constructed 42*84
    for i in range(42):
        for j in range(84):
            A[i][j] = " "
    for i in range(42):
        for j in range(84):
            if(i < 2) or (i > 39):
                A[i][j] = "X"
            elif(j < 4) or (j > 79):
                A[i][j] = "X"
            if(i % 4 == 0) and (j % 8 == 0):
                for k in range(2):  # populating wall block
                    for l in range(4):
                        A[i + k][j + l] = "X"

    for i in range(
            1,
            20):  # random wall blocks are inserted in between in the board (if its inserted in such a way that no way of
        # getting through exitgate please restart the game.) this is to give a
        # feeling of map in the board.
        ra = random.randint(1, 2)
        for j in range(ra):
            en_y = 4 * random.randint(2, 18)
            if A[2 *
                 i][en_y] == "X" or A[2 *
                                      i][en_y] == "B" or A[2 *
                                                           i][en_y] == "/":
                pass
            else:
                for k in range(2):  # populating wall block
                    for l in range(4):
                        A[2 * i + k][en_y + l] = "X"

# inserting bricks randomly such that there are min 3 and max 4 bricks are
# in each column.


def insert_bricks(A):
    for i in range(1, 20):
        ra = random.randint(3, 5)
        for j in range(ra):
            en_y = 4 * random.randint(2, 19)
            if A[2 *
                 i][en_y] == "X" or A[2 *
                                      i][en_y] == "B" or A[2 *
                                                           i][en_y] == "/":
                pass
            else:
                for k in range(2):  # populating wall block
                    for l in range(4):
                        A[2 * i + k][en_y + l] = "/"
