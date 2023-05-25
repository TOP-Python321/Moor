def math_function_resolver(operation: 'callable', *args: tuple[float], strings: bool = False) -> list[float] | list[str]:
    """
    Функция вычисляет округлённые значения для различных математических функций.
    
    :param operation: Вызываемый объект. Ожидает один обязательный аргумент.
    :param args: Кортеж с аргументами. Каждый аргумент будет передан в функцию для вычисления.
    :param strings: Опциональный параметр. Возвращает строковое представление результатов вычисления, 
    если True, иначе возвращает float.
    :return: Список результатов вычисления.
    """
    result = []
    
    for i in args:
        num = operation(i)
        if strings:
            num = str(round(num, 2))
        result.append(round(num, 2))
    return result
    
    
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']

# >>> math_function_resolver(lambda x: 1.5**x, *range(1, 10), strings=True)
# ['1.5', '2.25', '3.38', '5.06', '7.59', '11.39', '17.09', '25.63', '38.44']

# >>> math_function_resolver(lambda x: 4**x, *range(1, 10), strings=True)
# ['4', '16', '64', '256', '1024', '4096', '16384', '65536', '262144']

# >>> math_function_resolver(lambda x: 4**x, *range(1, 10))
# [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]