from math import sqrt


class Tetrahedron:
    """
    Описывает правильный тетраэдр.
    """
    def __init__(self, edge: float):
        self.edge = float(edge)

    def surface(self) -> float:
        """ Вычисляет площадь поверхности. """
        square = sqrt(3) * self.edge ** 2
        return square

    def volume(self) -> float:
        """ Вычисляет объём тела. """
        vol = (self.edge ** 3) / 12 * sqrt(2)
        return vol


# t1 = Tetrahedron(7)
# t1.edge
# 7.0
# t1.surface()
# 84.87048957087498
# t1.volume()
# 40.42293765783097
# t1.edge = 8
# t1.surface()
# 110.85125168440814
# t1.volume()
# 60.339778661252055