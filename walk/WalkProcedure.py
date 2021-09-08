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
        plt.scatter(self.__x, self.__y, c='black',edgecolor='white', s=30)
        plt.scatter(4, 1, c='red', s=100)  # J
        plt.scatter(3, 2, c='red', s=100)  # F
        plt.scatter(6, 2, c='red', s=100)  # H
        plt.scatter(2, 3, c='red', s=100)  # C
        plt.scatter(1, 4, c='red', s=100)  # E
        plt.scatter(3, 4, c='red', s=100)  # B
        plt.scatter(5, 4, c='red', s=100)  # I
        plt.scatter(2, 5, c='red', s=100)  # A
        plt.scatter(5, 5, c='red', s=100)  # G
        plt.scatter(3, 6, c='red', s=100)  # D
        # Start Walk Position
        pos = np.array([1, 1])

        # Arrays/Lists to store some positions to draw them later.
        pos_x = []
        pos_y = []

        move_list = []

        pos_x.append(pos[0])
        pos_y.append(pos[1])

        # Simulate the random walk upto nsteps steps
        nsteps = 20

        # Sensors Configuration
        sendor_path = DetectSensor()
        sendor_path.sendor_accuracy = 90

        sensor_item = DetectSensor()
        sensor_item.sendor_accuracy = 90

        for i in range(nsteps):
            plt.scatter(self.__x, self.__y, c='black', edgecolor='white',s=30)
            randno = np.random.random_integers(1, 4)
            if randno == 1:  # Move To Right
                if pos[0] < 6 :
                    pos = pos + [1, 0]
            elif randno == 2 :  # Up
                if pos[1] < 6 :
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
            plt.plot(pos_x, pos_y,alpha=0.3, c='green', linewidth=3)
            move_list.append([pos_x[-1],pos_y[-1]])


            print(pos_x[-1],pos_y[-1])


            # Pause for animation
            plt.pause(0.5)

        #plt.show()
        print(move_list)
