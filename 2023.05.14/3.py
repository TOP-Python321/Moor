def numbers_strip(sample: list, n: int = 1, copy: bool = False) -> list:
    """
    Returns a list with the 'n' minimum and maximum numbers removed. 
    If copy=True - returns a copy of the list
    """
    for _ in range(n):
        # КОММЕНТАРИЙ: метод remove() изменяет список, к которому применяется
        sample.remove(min(sample))
        sample.remove(max(sample))
    # ИСПРАВИТЬ: поэтому при постфактум проверке, даже если copy=True, вы уже изменили исходный список (см. пример ниже)
    if copy:
        return sample.copy()
    else:
        return sample


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> sample
# КОММЕНТАРИЙ: при copy=True этот список должен остаться неизменным
# [2, 3]

# >>> sample = [10, 20, 25, 40, 90, 110, 120]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [25, 40, 90]
# >>> sample is sample_stripped
# False


# ИТОГ: доработать — 2/4
