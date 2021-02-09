class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        print(f"Масса асфальта: {self._length * self._width * 25 * 5 / 1000} тн")
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(20, 5000, 125)
print(r.mass())
