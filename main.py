import numpy as np
from random import randrange, randint
from walk.WalkProcedure import RandomWalk
import matplotlib.pyplot as plt

def layout1():
    walk = RandomWalk(1)
    __product_count = 10
    start_position = [0, 0]
    result = []
    path_trace = []
    freq = np.zeros((6, 6))
    #Visualization

    order_count = randint(1, __product_count)
    orders = list(np.random.permutation(np.arange(1, __product_count))[:order_count])
    print(orders)
    score, start_position, total_path = walk.walk_simulate(start_position, orders, True)

    for i in range(1, 1000):
        order_count = randint(1, __product_count)
        orders = list(np.random.permutation(np.arange(1, __product_count))[:order_count])
        score, start_position, total_path = walk.walk_simulate(start_position, orders, False)
        # for p in total_path:
        #     freq[p[0]][p[1]] += 1
        #
        #
        result.append(score)
        path_trace.append(total_path)
    # plt.imshow(freq/1000)
    # plt.show()
    # print(freq/1000)
    # print((36 - np.sum(freq/1000)))
    print(f"Average Score is: {np.average(result)}")
    print(f"Min Score is: {np.min(result)}")
    print(f"Min Path Length is: {min(map(len, path_trace))}")
    print(f"Min Path is: {path_trace[path_trace.index(min(path_trace, key=len))]}")

    print(f"Max Score is: {np.max(result)}")
    print(f"Max Path Length is: {max(map(len, path_trace))}")
    print(f"Max Path is: {path_trace[path_trace.index(max(path_trace, key=len))]}")


def layout2():
    walk = RandomWalk(2)
    __product_count = 16
    start_position = [0, 0]
    result = []
    orders_list = range(1, __product_count)
    path_trace = []

    #Visualization

    # order_count = randint(1, __product_count)
    # orders = list(np.random.permutation(np.arange(1, __product_count))[:order_count])
    # print(orders)
    # score, start_position, total_path = walk.walk_simulate(start_position, orders, True)

    for i in range(1, 1000):
        order_count = randint(1, __product_count)
        orders = list(np.random.permutation(np.arange(1, __product_count))[:order_count])
        score, start_position, total_path = walk.walk_simulate(start_position, orders, False)
        result.append(score)
        path_trace.append(total_path)

    print(f"Average Score is: {np.average(result)}")
    print(f"Min Score is: {np.min(result)}")
    print(f"Min Path Length is: {min(map(len, path_trace))}")
    print(f"Min Path is: {path_trace[path_trace.index(min(path_trace, key=len))]}")

    print(f"Max Score is: {np.max(result)}")
    print(f"Max Path Length is: {max(map(len, path_trace))}")
    print(f"Max Path is: {path_trace[path_trace.index(max(path_trace, key=len))]}")


if __name__ == '__main__':
    print('*************Layout1***************')
    layout1()

    # print('*************Layout2***************')
    # layout2()
