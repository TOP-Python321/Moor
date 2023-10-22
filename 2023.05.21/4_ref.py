def repeat(count: int = 2) -> 'function':
    def decorator(func) -> 'function':
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


# >>> @repeat(5)
# ... def testing_function():
# ...     print('python')
# ...
# >>>
# >>> testing_function()
# python
# python
# python
# python
# python
