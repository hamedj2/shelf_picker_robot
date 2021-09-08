import matplotlib.pyplot as plt
import numpy as np
from robotconfigs.Sensors import DetectSensor
from random import randrange


class RandomWalk:
    # ClasS Initialize
    def __init__(self):
        self.__path_sensor = DetectSensor()
        self.__path_sensor.sendor_accuracy = 90

        self.__x = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5,
                    5, 5, 5]
        self.__y = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2,
                    3, 4, 5]

        self.__data = np.zeros([6, 6])
        self.__data[3, 0] = 1
        self.__data[2, 1] = 2
        self.__data[5, 1] = 3
        self.__data[1, 2] = 4
        self.__data[0, 3] = 5
        self.__data[2, 3] = 6
        self.__data[4, 3] = 7
        self.__data[1, 4] = 8
        self.__data[4, 4] = 9
        self.__data[2, 5] = 10

    def check_valid_position(self, new_pos):
        if new_pos[1] < 0 or new_pos[1] > 5:
            return False
        elif new_pos[0] < 0 or new_pos[0] > 5:
            return False
        else:
            if 1 <= self.__data[new_pos[0], new_pos[1]] <= 10:
                self.__path_sensor.sense()
                if self.__path_sensor.sendor_data is True:
                    return True
                else:
                    return False
            else:
                return False

    def walk_simulate(self):
        plt.title('Random walk of Bob')
        # plt.scatter(self.__x, self.__y, c='black', s=30)
        # x, y = self.__data.T
        # plt.scatter(x, y, c='red', s=100)
        plt.matshow(self.__data, cmap='gray')

        # Start Walk Position
        pos = np.array([0, 0])

        # Arrays/Lists to store some positions to draw them later.
        pos_x = []
        pos_y = []

        move_list = []

        pos_x.append(pos[0])
        pos_y.append(pos[1])

        # Simulate the random walk upto nsteps steps
        nsteps = 100000
        # Sensors Configuration
        sendor_path = DetectSensor()
        sendor_path.sendor_accuracy = 90

        sensor_item = DetectSensor()
        sensor_item.sendor_accuracy = 90

        for i in range(nsteps):
            # plt.scatter(self.__x, self.__y, c='black', edgecolor='white', s=30)

            plt.matshow(self.__data, cmap='gray')

            # Get neighbor cells
            up_pos = [-99, -99]
            down_pos = [-99, -99]
            left_pos = [-99, -99]
            right_pos = [-99, -99]

            # Get valid neighbor
            path = []
            if self.check_valid_position(pos - [0, 1]):
                up_pos = pos - [0, 1]
                path.append(up_pos)
            if self.check_valid_position(pos + [0, 1]):
                down_pos = pos + [0, 1]
                path.append(down_pos)
            if self.check_valid_position(pos - [1, 0]):
                left_pos = pos - [1, 0]
                path.append(left_pos)
            if self.check_valid_position(pos + [1, 0]):
                right_pos = pos + [1, 0]
                path.append(right_pos)

            if path.__len__() == 1:
                pos = path[0]
            elif path.__len__() > 1:
                random_index = randrange(len(path))
                pos = path[random_index]
            else:
                randno1 = np.random.random_integers(1, 4)
                if randno1 == 1:  # Move To Right
                    if pos[0] < 5:
                        pos = pos + [1, 0]
                elif randno1 == 2:  # Up
                    if pos[1] > 0:
                        pos = pos - [0, 1]
                if randno1 == 3:  # Left
                    if pos[0] > 0:
                        pos = pos - [1, 0]
                elif randno1 == 4:  # Down
                    if pos[1] < 5:
                        pos = pos + [0, 1]

            pos_x.append(pos[0])
            pos_y.append(pos[1])
            # Draw the paths
            plt.plot(pos_x, pos_y, c='yellow', linewidth=5)
            # Pause for animation
            plt.pause(0.5)

        plt.show()
        print(move_list)
