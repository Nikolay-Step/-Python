# task 4


class Car:
    def __init__(self, color, name, is_police, speed):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def show_speed(self):
        print(self.speed)

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print('машина повернула ' + direction)


class TownCar(Car):
    def show_speed(self):
        self.speed = 130
        if self.speed > 60:
            print('Speed limit')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        self.speed = 60
        print(self.speed)


w = TownCar('white', 'vedro', 'true', 70)
print(w.show_speed())
