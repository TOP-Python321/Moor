def numbers_strip(sample: list, n: int = 1, copy: bool = False) -> list:
    """
    Returns a list with the 'n' minimum and maximum numbers removed. 
    If copy=True - returns a copy of the list
    """
    if copy:
        sample_copy = sample.copy()
    else:
        sample_copy = sample
    
        # КОММЕНТАРИЙ: метод remove() изменяет список, к которому применяется
    # ИСПРАВИТЬ: поэтому при постфактум проверке, даже если copy=True, вы уже изменили исходный список (см. пример ниже)
    return sample_copy[n:-n]


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> sample
# КОММЕНТАРИЙ: при copy=True этот список должен остаться неизменным
# [2, 3]

# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> sample
# [2, 3]
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample, copy=True)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# False
# >>> sample
# [1, 2, 3, 4]


# ИТОГ: доработать — 2/4
