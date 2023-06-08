from collections.abc import Iterable


def product(numbers: Iterable[float]) -> float:
    """
    Функция вычисляет произведение чисел в переданном объекте.
    
    :param numbers: Итерируемый объект с числами в качестве элементов.
    
    :return: Float. Произведение всех чисел переданного аргумента.
    """
    if len(numbers) == 0:
        return 1
    elif 0 in numbers:
        return 0.0
    return float(numbers[0]) * product(numbers[1:])