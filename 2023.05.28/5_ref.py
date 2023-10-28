from datetime import datetime as dt

import utils_ref

log_path = utils_ref.DATA_DIR / 'function_calls.log'


def logger(func_obj: 'function') -> 'function':
    if func_obj.__defaults__ is None:
        func_obj.__defaults__ = ()
    if func_obj.__kwdefaults__ is None:
        func_obj.__kwdefaults__ = {}
    
    def wrapper(*args, **kwargs):
        flag_exc = False
        timestamp = dt.now()
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
        with open(log_path, 'a', encoding='utf-8') as fileout:
            print(
                (f'{timestamp:%Y.%m.%d %H:%M:%S}'
                 f' — {func_obj.__name__}({args}{ins1}{kwargs})'
                 f' {ins2} {result}'), 
                file=fileout
            )
        return result
    
    return wrapper


# >>> @logger
# ... def test1(a, b, c):
# ...     print(f'PRINT: {a=}, {b=}, {c=}')
# ... 
# >>> 
# >>> test1(1, 2, 7)
# PRINT: a=1, b=2, c=7
# >>>
# >>> print(log_path.read_text())
# 2023.10.28 23:05:08 — test1(1, 2, 7) -> None
# 
# >>>
