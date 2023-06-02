from datetime import datetime as dt


def logger(func: 'callable') -> 'callable':
    """
    Декоратор, сохраняющий журнал вызовов декорируемой функции в файл.
    """
    def wrapper(*args, **kwargs):
        now = dt.now()
        today = now.strftime('%Y.%m.%d %H:%M:%S')
        
        with open('data\\function_calls.log', 'a', encoding='utf-8') as file:
        
            log = []
            log.append(f"{func.__name__}(")
            file.write(today + " - ")

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
            file.write(func_with_args + ' -> ')

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                file.write(f"\t {type(e).__name__}: {str(e)}\n")
                return

            if result is not None:
                file.write(f"{result}\n")
            else:
                file.write(f"{None}\n")

        return result

    return wrapper
    
    
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(45, 12, digits=2)
# 3.75

# >>> def total(num1, num2, *, digits=0, number=5):
# ...     return round(num1 + num2 * number, digits)
# ...
# >>> total = logger(total)
# >>> total(8, 4, number=7)

# >>> def test_func():
# ...     pass
# ...
# >>> test_func = logger(test_func)
# >>> test_func()

# 15:00:12 > type data\function_calls.log
# 2023.06.01 14:50:11 - div_round(45, 12, digits=2) -> 3.75
# 2023.06.01 14:53:14 - total(8, 4, number=7, digits=0) -> 36
# 2023.06.01 15:00:06 - test_func() -> None