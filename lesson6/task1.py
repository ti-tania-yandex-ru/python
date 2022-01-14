from itertools import cycle
from time import sleep


class TrafficLights:
    colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.colors)
        for item in my_cycle:
            if self.__color == item:
                print(item)
                sleep(self.colors[item])
                self.__color = next(my_cycle)


light = TrafficLights('Желтый')
light.running()
