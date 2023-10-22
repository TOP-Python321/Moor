def logger(func: 'callable') -> 'callable':
    """
    Декоратор, выводящий в стандартный поток вывода журнал вызовов декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        log = []
        log.append(f"{func.__name__}(")

        for i in args:
            log.append(repr(i) + ", ")

        for key, value in kwargs.items():
            log.append(f"{key}={value}, ")

        if func.__defaults__ is not None:
            for default in func.__defaults__:
                log.append(f"{default}" + ", ")

        if func.__kwdefaults__ is not None:
            for key, value in func.__kwdefaults__.items():
                if key not in kwargs:
                    log.append(f"{key}={value}, ")
                    
        log[-1] = log[-1].rstrip(", ") + ")"
        func_with_args = ''.join(log)
        print(func_with_args, end=' -> ')

        try:
            # ИСПРАВИТЬ: вызов функции должен или предшествовать всему выводу декоратора, или следовать уже после всего вывода декоратора — не посередине
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"\t {type(e).__name__}: {str(e)}")
            return

        if result is not None:
            print(result)
        else:
            print()

        return result

    return wrapper
    
    
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>> div_round(5, 8, digits=2)
# div_round(5, 8, digits=2) -> 0.62
# 0.62

# >>> def repeat(word, sign):
# ...     return word * sign
# ...
# >>> repeat = logger(repeat)
# >>>
# >>> repeat('hello', 5)
# repeat('hello', 5) -> hellohellohellohellohello
# 'hellohellohellohellohello'

# КОММЕНТАРИЙ: мало сценариев объявления и вызова декорируемой функции рассмотрено

# СДЕЛАТЬ: изучите пример, запустите тестовые функции со своей реализацией декоратора, найдите ошибки


# ИТОГ: нужно лучше, доработайте — 3/6
