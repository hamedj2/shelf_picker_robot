import random


class DetectShelveSensor:
    def __init__(self):
        self.__sendor_accuracy = 0
        self.__sendor_data = -1

    def set_sensor_accuarcy(self, sendor_accuracy):
        self.__sendor_accuracy = sendor_accuracy

    def get_sensor_accuarcy(self):
        return self.__sendor_accuracy

    def get_sendor_data(self):
        return self.__sendor_data

    def sense(self):
        if random.random() <= 0.8:
            self.__sendor_data = 1
        else:
            self.__sendor_data = 0

    # Class Property
    sendor_accuracy = property(get_sensor_accuarcy, set_sensor_accuarcy)
    sendor_data = property(get_sendor_data)
