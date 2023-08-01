class Point:
    """
    Описывает двумерную точку.
    """
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        raise TypeError("'Point' object does not support coordinate assignment")

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        raise TypeError("'Point' object does not support coordinate assignment")


class Line:
    """
    Описывает отрезок.
    """
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length: float = self.length_calc(start, end)

    @staticmethod
    def length_calc(point1: Point, point2: Point) -> float:
        """
        Расчитывает расстояние между точками start и end.
        :param point1: начальная точка
        :param point2: конечная точка
        :return: расстояние между точками
        """
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

    def __repr__(self):
        return f"{str(self.start)}———{str(self.end)}"

    def __str__(self):
        return f"{str(self.start)}———{str(self.end)}"

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value):
        if isinstance(value, Point):
            self._start = value
            self._length = self.length_calc(self.start, self.end)
        else:
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value):
        if isinstance(value, Point):
            self._end = value
            self._length = self.length_calc(self.start, self.end)
        else:
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        raise TypeError("'Line' object does not support length assignment")


class Polygon(list):
    """
    Описывает многоугольник.
    """
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        super().__init__([side1, side2, side3, *sides])

    @property
    def perimeter(self) -> float:
        """
        Вычисляет периметр многоугольника.
        :return: периметр
        """
        if not self.is_closed():
            raise ValueError("line items doesn't form a closed polygon")
        return sum(line.length for line in self)

    def is_closed(self) -> bool:
        """
        Проверяет, формируют ли отрезки замкнутый многоугольник.
        :return: True|False
        """
        if len(self) < 3:
            return False
        return self[0].start == self[-1].end and all(self[i].end == self[i + 1].start for i in range(len(self) - 1))

# >>> p1 = Point(3, 6)
# >>> p2 = Point(7, 3)
# >>> p3 = Point(11, 6)
# >>>
# >>> p1
# (3, 6)
# >>>
# >>> repr(p1) == str(p1)
# True
# >>>
# >>> p1 == Point(3, 6)
# True
# >>>
# >>> p1.x, p1.y
# (3, 6)
# >>>
# >>> p2.y = 5
# TypeError: 'Point' object does not support coordinate assignment
# >>>
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>>
# >>> l1
# (3, 6)———(7, 3)
# >>>
# >>> repr(l1) == str(l1)
# True
# >>>
# >>> l1.length
# 5.0
# >>>
# >>> l1.length = 10
# TypeError: 'Line' object does not support length assignment
# >>>
# >>> l3.start = 12
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>>
# >>> pol1 = Polygon(l1, l2, l3)
# >>> pol1.perimeter
# 18.0
# >>>
# >>> pol1.perimeter = 20
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>>
# >>> l3.end = Point(1, 6)
# >>> pol1[-1] = l3
# >>> pol1.perimeter
# ValueError: line items doesn't form a closed polygon
