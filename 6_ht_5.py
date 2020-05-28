# task 5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('письмо')


class Pencil(Stationery):
    def draw(self):
        print('рисунок')


class Handle(Stationery):
    def draw(self):
        print('флипчарт')


p = Pen('pen')
print(p.draw())
