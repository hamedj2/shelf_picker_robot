import numpy as np
from random import randrange
from prettytable import PrettyTable
import pandas as pd

from robotconfig.Sensors import DetectShelveSensor


def solution1():
    long_memory = [0] * 5

    grid = np.empty(shape=(6, 6), dtype=np.dtype(str))
    grid.fill(0)

    n = 6
    m = 6
    short_memory = [[0] * m] * n
    print(short_memory)

    cell_memory = {
        "last_position": 0,  # index number or grid number
        "penalty": 0,  # -1, 3
        "visited": 0  # 0,1
    }
    cell_memory1 = {
        "last_position": 0,  # index number or grid number
        "penalty": -1,  # -1, 3
        "visited": 1  # 0,1
    }
    short_memory[1][1] = cell_memory1

    cell_memory2 = {
        "last_position": 0,  # index number or grid number
        "penalty": -1,  # -1, 3
        "visited": 1  # 0,1
    }

    short_memory[1][2] = cell_memory2

    cell_memory3 = {
        "last_position": 3,  # index number or grid number
        "penalty": 3,  # -1, 3
        "visited": 1  # 0,1
    }

    short_memory[1][3] = cell_memory3

    long_memory[1] = short_memory
    long_memory[2] = short_memory
    long_memory[3] = short_memory

    df = pd.DataFrame(long_memory)

    p = PrettyTable()
    for row in short_memory:
        p.add_row(row)

    print(p.get_string(header=False, border=False))
    # for i in range(1, 1000):
    #     grid.fill(0)  # reset the memory
    #
    # x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # grid[0, 0] = 'p'
    # grid[0, 2] = 'D'
    # grid[1, 1] = 'A'
    # grid[1, 4] = 'G'
    # grid[2, 0] = 'E'
    # grid[2, 2] = 'B'
    # grid[2, 4] = 'I'
    # grid[3, 1] = 'C'
    # grid[4, 2] = 'F'
    # grid[4, 5] = 'H'
    # grid[5, 3] = 'J'
    # print(grid)
    # print("--------------------------------------------------")


def solution2():
    grid2 = [[0 for i in range(6)] for j in range(6)]
    grid2[0][0] = "p"
    for i in range(6):
        grid2[randrange(6)][randrange(1, 6)] = 1
    print(grid2)


if __name__ == '__main__':
    # solution1()
    # solution2()
    sendor = DetectShelveSensor()
    sendor.sendor_accuracy = 80
    sendor.sense()
    print(sendor.sendor_data)
