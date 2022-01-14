class Road:
    weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, depth):
        print(
            f'Масса асфальта дороги длиной {self._length}м, шириной {self._width}м и толщиной асфальта'
            f' {depth}cм равна {self._width * self._length * Road.weight * depth / 1000}т')


road = Road(1000, 20)
road.mass(10)
