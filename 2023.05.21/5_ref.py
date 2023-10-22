def logger(func_obj: 'function') -> 'function':
    if func_obj.__defaults__ is None:
        func_obj.__defaults__ = ()
    if func_obj.__kwdefaults__ is None:
        func_obj.__kwdefaults__ = {}

    def wrapper(*args, **kwargs):
        flag_exc = False
        try:
            result = func_obj(*args, **kwargs)
        except Exception as exc:
            result = f'{exc.__class__.__name__}: {exc}'
            flag_exc = True

        i = len(args) - func_obj.__code__.co_argcount
        args = ', '.join(
            str(arg)
            for arg in args + (func_obj.__defaults__[i:] if i else ())
        )
        kwargs = ', '.join(
            f'{key}={val}'
            for key, val in (func_obj.__kwdefaults__ | kwargs).items()
        )

        ins1 = ', ' if args and kwargs else ''
        ins2 = '..' if flag_exc else '->'
        print(f'{func_obj.__name__}({args}{ins1}{kwargs}) {ins2} {result}')
        return result

    return wrapper


# >>> @logger
# ... def test1(a, b, c):
# ...     print(f'PRINT: {a=}, {b=}, {c=}')
# ...
# >>>
# >>> @logger
# >>> def test2(a=0, b=1, c=2):
# ...     print(f'PRINT: {a=}, {b=}, {c=}')
# ...     return a + b / c
# ...
# >>>
# >>> @logger
# >>> def test3(a, b=3, *, c=4, d=5):
# ...     print(f'PRINT: {a=}, {b=}, {c=}, {d=}')
# ...
# >>>
# >>> @logger
# ... def test4(*a, b=7) -> None:
# ...     print(f'PRINT: {a=}, {b=}')
# ...
# >>>

# >>> test1(10, 20, 30)
# PRINT: a=10, b=20, c=30
# test1(10, 20, 30) -> None
# >>>
# >>> test1(c=9, a=2, b=12)
# PRINT: a=2, b=12, c=9
# test1(c=9, a=2, b=12) -> None

# >>> test2(4, 6, 2)
# PRINT: a=4, b=6, c=2
# test2(4, 6, 2) -> 7.0
# 7.0
# >>>
# >>> test2(3, 4)
# PRINT: a=3, b=4, c=2
# test2(3, 4, 2) -> 5.0
# 5.0
# >>>
# >>> test2(4)
# PRINT: a=4, b=1, c=2
# test2(4, 1, 2) -> 4.5
# 4.5
# >>>
# >>> test2()
# PRINT: a=0, b=1, c=2
# test2(0, 1, 2) -> 0.5
# 0.5
# >>>
# >>> test2(3, c=1)
# PRINT: a=3, b=1, c=1
# test2(3, 1, c=1) -> 4.0
# 4.0
# >>>
# >>> test2(c=0)
# PRINT: a=0, b=1, c=0
# test2(0, 1, 2, c=0) .. ZeroDivisionError: division by zero
# '.. ZeroDivisionError: division by zero'

# >>> test3(1)
# PRINT: a=1, b=3, c=4, d=5
# test3(1, 3, c=4, d=5) -> None
# >>>
# >>> test3(1, 4)
# PRINT: a=1, b=4, c=4, d=5
# test3(1, 4, c=4, d=5) -> None
# >>>
# >>> test3(1, 4, d=9)
# PRINT: a=1, b=4, c=4, d=9
# test3(1, 4, c=4, d=9) -> None
# >>>
# >>> test3(1, 4, c=8)
# PRINT: a=1, b=4, c=8, d=5
# test3(1, 4, c=8, d=5) -> None

# >>> test4(1,2,3)
# PRINT: a=(1, 2, 3), b=7
# test4(1, 2, 3, b=7) -> None
# >>>
# >>> test4()
# PRINT: a=(), b=7
# test4(b=7) -> None
# >>>
# >>> test4(b=1)
# PRINT: a=(), b=1
# test4(b=1) -> None


# данная реализация декоратора работает только в 94% сценариях объявления и вызова декорируемой функции; для сценария ниже требуется заметное усложнение декоратора
# >>> test3(1, b=2)
# PRINT: a=1, b=2, c=4, d=5
# test3(1, 3, c=4, d=5, b=2) -> None
