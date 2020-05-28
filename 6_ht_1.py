# task 1
import time


class TrafficLight:
    __color = 'red'

    def running():
        x = 1
        while x < 15:
            if x == 1:
                print(TrafficLight.__color)
                time.sleep(7)
                TrafficLight.__color = 'yellow'
                print(TrafficLight.__color)
                time.sleep(2)
                TrafficLight.__color = 'green'
                print(TrafficLight.__color)
            elif x > 1:
                time.sleep(7)
                TrafficLight.__color = 'red'
                print(TrafficLight.__color)
                time.sleep(2)
                TrafficLight.__color = 'yellow'
                print(TrafficLight.__color)
                time.sleep(7)
                TrafficLight.__color = 'green'
                print(TrafficLight.__color)
            x += 1


print(TrafficLight.running())
