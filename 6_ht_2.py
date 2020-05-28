# task 2


class Road:
    _length = 0
    _width = 0

    def road_mass(self, w, l):
        self._width = w
        self._length = l
        print('Масса асфальта: ' + str(w*l*25*10) + ' киллограм')


r = Road()
r.road_mass(10, 100)

