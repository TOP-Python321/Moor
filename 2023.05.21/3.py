def round_string(num: float) -> str:
    return str(round(num))


def math_function_resolver(
        operation: 'callable',
        # ИСПРАВИТЬ: для произвольного кортежа аргументов всегда аннотируется сразу тип элементов
        *args: float,
        strings: bool = False
) -> list[int | str]:
    """
    Функция вычисляет округлённые значения для различных математических функций.
    
    :param operation: Вызываемый объект. Ожидает один обязательный аргумент.
    :param args: Кортеж с аргументами. Каждый аргумент будет передан в функцию для вычисления.
    :param strings: Опциональный параметр. Возвращает строковое представление результатов вычисления, 
    если True, иначе возвращает float.
    :return: Список результатов вычисления.
    """
        # КОММЕНТАРИЙ: без этой проверки на каждой итерации желательно бы обойтись
        # ИСПРАВИТЬ: ошибка (см. тест ниже)
    converting = round_string if strings else round
    return [converting(operation(num)) for num in args]


# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']

# >>> math_function_resolver(lambda x: 1.5**x, *range(1, 10), strings=True)
# КОММЕНТАРИЙ: у вас не такой результат для этого теста
# ['2', '2', '3', '5', '8', '11', '17', '26', '38']
# КОММЕНТАРИЙ: а вот такой
# TypeError: type str doesn't define __round__ method

# >>> math_function_resolver(lambda x: 4**x, *range(1, 10), strings=True)
# ['4', '16', '64', '256', '1024', '4096', '16384', '65536', '262144']

# >>> math_function_resolver(lambda x: 4**x, *range(1, 10))
# [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]


# ИТОГ: нужно лучше, доработать — 2/5
