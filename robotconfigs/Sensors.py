import random


# Class Detection
class DetectSensor:
    # Class Initialize
    def __init__(self):
        self.__sendor_accuracy = 0
        self.__sendor_data = -1

    # Read From Private Variable
    def get_sensor_accuarcy(self):
        return self.__sendor_accuracy

    # Write Into Private Method
    def set_sensor_accuarcy(self, sendor_accuracy):
        if sendor_accuracy < 70:
            self.__sendor_accuracy = 90
        else:
            self.__sendor_accuracy = sendor_accuracy

    # Read From Private Variable
    def get_sendor_data(self):
        return self.__sendor_data

    # Send Pulse Detection To Sensor
    def sense(self):
        if random.random() <= self.sendor_accuracy / 100:
            # Correct Detection
            self.__sendor_data = True
        else:
            # Incorrect Detection
            self.__sendor_data = False

    # Class Property
    # Property With Read and Write Access
    sendor_accuracy = property(get_sensor_accuarcy, set_sensor_accuarcy)

    # Read Only Property
    sendor_data = property(get_sendor_data)
