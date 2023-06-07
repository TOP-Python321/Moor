# ИСПРАВИТЬ: согласно условию, функция должна принять минимум два числа — а сейчас её можно вызвать и вовсе не передав ни одного аргумента, или передав только один (см. пример ниже)
# ИСПОЛЬЗОВАТЬ: для произвольного кортежа позиционных аргументов аннотируется сразу тип элементов (кортежем-то он всегда будет)
def central_tendency(num1: float, num2: float, *others_num: float) -> dict[str, float]:
    """
    Returns a dictionary with computed central trend measure values
    """
    sample = sorted((num1, num2) + others_num)
    length_of_tuple = len(sample)
    i_half = length_of_tuple // 2
    arithmetic = sum(sample) / length_of_tuple
    multiplied = 1
    numerator_sum = 0
    
    if length_of_tuple % 2:
        median = float(sample[i_half])
    else:
        median = sum(sample[i_half-1:i_half+1]) / 2

    # ПЕРЕИМЕНОВАТЬ: имена i, j, k — только для индексов!
    for num in sample:
        # КОММЕНТАРИЙ: очень хороший подход через один цикл!
        multiplied *= num
        numerator_sum += 1 / num
    geometric = multiplied ** (1/length_of_tuple)
    harmonic = length_of_tuple / numerator_sum
    
    tendency = {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }
                
    return tendency


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1, 2, 3, 4, 56, 10, 5)
# {'median': 4, 'arithmetic': 11.571428571428571, 'geometric': 4.8935517101149655, 'harmonic': 2.915220624690134}
# >>> central_tendency(1, 2, 3, 4, 56, 10, 5, 8)
# {'median': 4.5, 'arithmetic': 11.125, 'geometric': 5.203641966051238, 'harmonic': 3.166823751178134}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

# >>> central_tendency()
# ...
# КОММЕНТАРИЙ: а должно быть TypeError из-за пропущенных обязательных аргументов
# ZeroDivisionError: division by zero

# >>> central_tendency()
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: central_tendency() missing 2 required positional arguments: 'num1' and 'num2'

# ИТОГ: хорошо, доработать — 4/6
