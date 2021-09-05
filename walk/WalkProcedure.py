import matplotlib.pyplot as plt
import numpy as np
from robotconfigs.Sensors import DetectShelveSensor


class RandomWalk:
    def __init__(self):
        self.__x__ = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6,
                      6, 6, 6]
        self.__y__ = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3,
                      4, 5, 6]

    def walk_simulate(self):
        plt.scatter(self.__x__, self.__y__, c='black', s=50)
        plt.title('Random walk of Alice')
        pos = np.array([1, 1])  # Start Walk

        # Arrays/Lists to store some positions to draw them later.
        posX = []
        posY = []
        posX.append(pos[0])
        posY.append(pos[1])
        # Simulate the random walk upto nsteps steps
        nsteps = 1000000
        sendor = DetectShelveSensor()
        sendor.sendor_accuracy = 80

        for i in range(nsteps):
            plt.figure()
            plt.scatter(self.__x__, self.__y__, c='black', s=50)
            randno = np.random.random_integers(1, 4)
            if randno == 1:  # Right
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
            posX.append(pos[0])
            posY.append(pos[1])

            # Draw the paths
            plt.plot(posX, posY, c='red', linewidth=3)
            print(i)
            # Pause for animation
            plt.pause(0.5)

        plt.show()
