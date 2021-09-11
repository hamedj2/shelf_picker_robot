import matplotlib.pyplot as plt
import numpy as np
from robotconfigs.Sensors import DetectSensor
from random import randrange


class RandomWalk:
    # ClasS Initialize
    def __init__(self):
        self.__path_sensor = DetectSensor()
        self.__path_sensor.sendor_accuracy = 90
        self.__loop_detected = False
        self.__loop_count = 0

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

        self.__short_memory = np.zeros([6, 6])

    def check_valid_position(self, new_pos, orders):
        if new_pos[1] < 0 or new_pos[1] > 5:
            return False
        elif new_pos[0] < 0 or new_pos[0] > 5:
            return False
        elif self.__loop_detected:
            return True
        elif self.__short_memory[new_pos[0], new_pos[1]] == 1:
            return False
        else:
            if self.__data[new_pos[0], new_pos[1]] in orders:
                self.__path_sensor.sense()
                if self.__path_sensor.sendor_data is True:
                    return True
                else:
                    return False
            else:
                return False

    def walk_simulate(self, start_position, orders):
        # plt.title('Random walk of Bob')
        # plt.matshow(self.__data, cmap='gray')

        # Reset Short Memory
        self.__short_memory = np.zeros([6, 6])

        # Start Walk Position
        pos = np.array(start_position)

        # Arrays/Lists to store some positions to draw them later.
        pos_x = []
        pos_y = []

        step = 0
        pos_x.append(pos[0])
        pos_y.append(pos[1])

        # Sensors Configuration
        sendor_path = DetectSensor()
        sendor_path.sendor_accuracy = 90

        sensor_item = DetectSensor()
        sensor_item.sendor_accuracy = 90

        total_path = []
        see_item = []
        score = 0

        self.__loop_count = 0
        self.__loop_detected = False

        up_pos = [-99, -99]
        down_pos = [-99, -99]
        left_pos = [-99, -99]
        right_pos = [-99, -99]

        last_see_item = []
        while see_item.__len__() < len(orders):
            # plt.matshow(self.__data, cmap='gray')

            # Get valid neighbor
            path = []
            if self.check_valid_position(pos - [0, 1], orders):
                up_pos = pos - [0, 1]
                path.append(up_pos)
            if self.check_valid_position(pos + [0, 1], orders):
                down_pos = pos + [0, 1]
                path.append(down_pos)
            if self.check_valid_position(pos - [1, 0], orders):
                left_pos = pos - [1, 0]
                path.append(left_pos)
            if self.check_valid_position(pos + [1, 0], orders):
                right_pos = pos + [1, 0]
                path.append(right_pos)
            else:
                score -= 1

            if path.__len__() == 1:
                pos = path[0]
                if not self.__data[pos[0], pos[1]] in see_item:
                    score += 3
                    see_item.append(self.__data[pos[0], pos[1]])
            elif path.__len__() > 1:
                random_index = randrange(len(path))
                pos = path[random_index]
                if not self.__data[pos[0], pos[1]] in see_item:
                    score += 3
                    see_item.append(self.__data[pos[0], pos[1]])
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
            if pos[0] != 99 and pos[1] != 99:
                total_path.append(pos)
            # pos_x.append(pos[0])
            # pos_y.append(pos[1])
            self.__short_memory[pos[0], pos[1]] = 1

            if see_item == last_see_item:
                self.__loop_detected = True
                self.__loop_count = 0
            else:
                self.__loop_detected = False
            # plt.plot(pos_x, pos_y, c='yellow', linewidth=5)
            # plt.pause(0.1)
            if see_item.__len__() > 0:
                last_see_item = see_item
                # print(see_item)

            # plt.show()
        return score, pos, total_path
