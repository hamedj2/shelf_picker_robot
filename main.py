import numpy as np
from random import randrange, randint
from walk.WalkProcedure import RandomWalk

if __name__ == '__main__':
    walk = RandomWalk()
    start_position = [0, 0]
    result = []
    orders_list = range(1, 10)
    path_trace = []
    for i in range(1, 1000):
        order_count = randint(1, 10)
        orders = list(np.random.permutation(np.arange(1, 10))[:order_count])
        score, start_position, total_path = walk.walk_simulate(start_position, orders, False)
        result.append(score)
        path_trace.append(total_path.__len__())

        # print(f"Average Score is: {score}")
        # print(f"Order Count is: {orders.__len__()}")

    print(f"Average Score is: {np.average(result)}")
    print(f"Min Score is: {np.min(result)}")
    print(f"Max Score is: {np.max(result)}")
    print(f"Min Path is: {min(path_trace)}")
    print(f"Max Path is: {max(path_trace)}")
