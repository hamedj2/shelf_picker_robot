import random
import numpy as np
from random import randrange


def solution1():
    grid = np.empty(shape=(6, 6), dtype=np.dtype(str))
    grid.fill(0)
    x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    grid[0, 0] = 'p'
    grid[0, 2] = 'D'
    grid[1, 1] = 'A'
    grid[1, 4] = 'G'
    grid[2, 0] = 'E'
    grid[2, 2] = 'B'
    grid[2, 4] = 'I'
    grid[3, 1] = 'C'
    grid[4, 2] = 'F'
    grid[4, 5] = 'H'
    grid[5, 3] = 'J'
    print(grid)
    print("--------------------------------------------------")


def solution2():
    grid2 = [[0 for i in range(6)] for j in range(6)]
    grid2[0][0] = "p"
    for i in range(6):
        grid2[randrange(6)][randrange(1, 6)] = 1
    print(grid2)


if __name__ == '__main__':
    solution1()

    solution2()
