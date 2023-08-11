import math
import random
import string
from functools import singledispatch


@singledispatch
def data_insert(data):
    """
    Добавляет случайные данные в произвольную структуру данных.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return random.choice([True, False])


@data_insert.register(int)
def _(data) -> int:
    """
    Возвращает случайной целое число в диапазоне от -9 до 9.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return random.randint(-9, 9)


@data_insert.register(float)
def _(data) -> float:
    """
    Возвращает случайное число с плавающей точкой в диапазоне от -pi до pi.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return random.uniform(-math.pi, math.pi)


@data_insert.register(str)
def _(data) -> str:
    """
    Возвращает случайную строку длиной от 3 до 8 символов.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return ''.join(random.choices(string.ascii_letters, k=random.randint(3, 8)))


@data_insert.register(dict)
def _(data) -> dict:
    """
    Возвращает словарь с рандомными значениями.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return {key: data_insert(value) for key, value in data.items()}


@data_insert.register(list)
def _(data: list) -> list:
    """
    Возвращает список с рандомными значениями.
    :param data: Данные, для которых нужно вставить рандомные значения.
    :return: Рандомные значения в соответствии с указанным типом данных.
    """
    return [data_insert(item) for item in data]


# >>> n = ['', .0, {'k1': None, 'k2': ['', '']}, [0, 0]]
# >>>
# >>> data_insert(n)
# ['xwL', -2.8896449161730127, {'k1': True, 'k2': ['qmNmZdeN', 'eEYMiHx']}, [-6, 9]]
# >>>
# >>> n
# ['', 0.0, {'k1': None, 'k2': ['', '']}, [0, 0]]
# >>>
# >>> data_insert('')
# 'JwORP'
# >>>
# >>> data_insert(4)
# 5
# >>>
# >>> data_insert(1.2)
# 2.4268988800199462
