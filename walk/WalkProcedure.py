import matplotlib.pyplot as plt
import numpy as np
from robotconfigs.Sensors import DetectSensor


class RandomWalk:
    # ClasS Initialize
    def __init__(self):
        self.__x = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6,
                    6, 6, 6]
        self.__y = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3,
                    4, 5, 6]

    def walk_simulate(self):
        plt.title('Random walk of Bob')
        plt.scatter(self.__x, self.__y, c='black', s=50)

        # Start Walk Position
        pos = np.array([1, 1])

        # Arrays/Lists to store some positions to draw them later.
        pos_x = []
        pos_y = []
        pos_x.append(pos[0])
        pos_y.append(pos[1])

        # Simulate the random walk upto nsteps steps
        nsteps = 1000000

        # Sensors Configuration
        sendor_path = DetectSensor()
        sendor_path.sendor_accuracy = 90

        sensor_item = DetectSensor()
        sensor_item.sendor_accuracy = 90

        for i in range(nsteps):
            plt.scatter(self.__x, self.__y, c='black', s=50)

            randno = np.random.random_integers(1, 4)
            if randno == 1:  # Move To Right
                if pos[0] < 6:
                    pos = pos + [1, 0]
            elif randno == 2:  # Up
                if pos[1] < 6:
                    pos = pos + [0, 1]
            if randno == 3:  # Left
                if pos[0] > 1:
                    pos = pos - [1, 0]
            elif randno == 4:  # Down
                if pos[1] > 1:
                    pos = pos - [0, 1]
            pos_x.append(pos[0])
            pos_y.append(pos[1])

            # Draw the paths
            plt.plot(pos_x, pos_y, c='red', linewidth=3)

            # Pause for animation
            plt.pause(0.5)

        plt.show()
