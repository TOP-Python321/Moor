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
        return 0
    
    total = 1
    
    if isinstance(numbers, dict):
        numbers = list(numbers.values())

    for elem in numbers:
        if isinstance(elem, Iterable):
            total *= product(elem)
        else:
            total *= elem
        
    return float(total) 
    
    
# >>> product(range(10, 60, 10))
# 12000000.0
# >>>
# >>> product([0.12, 0.05, -0.09, 0.0, 0.21])
# 0.0
# >>>
# >>> product([0.12, 0.05, -0.09, 0.21, 1223, 523, 102])
# -7398.4607172
# >>>
# >>> product({'s': 9, 'b': [3, 4, 5]})
# 540.0
# >>>
# >>> product([])
# 1