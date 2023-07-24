import functools
import time


def exception_delay_repeat(func):
    """
    Декоратор повторяет вызов декорируемой функции в случае возникновения исключения через полсекунды.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            time.sleep(0.5)
            try:
                return func(*args, **kwargs)
            except Exception as e1:
                print(type(e).__name__ + ': ' + str(e))
                return None
    return wrapper

# >>> from random import randrange
# >>>
# >>> def test_func():
# ...     if randrange(2):
# ...         raise ConnectionError('failure')
# ...     else:
# ...         return 'success'
# ...
# >>> test_func
# <function test_func at 0x000001B226675DA0>
# >>> test_func = exception_delay_repeat(test_func)
# >>> test_func
# <function test_func at 0x000001B229350FE0>
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# 'success'
# >>> test_func()
# ConnectionError: failure
