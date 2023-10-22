def repeat(func: 'callable') -> 'callable':
    """
    Декоратор, повторяющий вызов функции 10 раз.
    
    :param func: Вызываемый объект.
    :return: Декорированная функция.
    """
    def wrapper(*args, **kwargs):
        for _ in range(10):
            print(func(*args, **kwargs))
    return wrapper


# >>> def testing_function():
# ...     return 'I WILL NOT SLEEP THROUGH MY EDUCATION'
# ...
# >>> testing_function = repeat(testing_function)
# >>> testing_function()
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION
# I WILL NOT SLEEP THROUGH MY EDUCATION


# ИТОГ: отлично — 3/3
