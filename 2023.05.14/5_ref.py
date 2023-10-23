def central_tendency(
        num1: float,
        num2: float,
        *numbers: float
) -> dict[str, float]:
    numbers = num1, num2, *numbers
    n = len(numbers)
    no_zero_flag = 0 not in numbers
    result = {
        'median': 0.0,
        'arithmetic': 0.0,
        'geometric': float(no_zero_flag),
        'harmonic': 0.0,
    }

    h = n // 2
    h = slice(h if n % 2 else h - 1, h + 1)
    result['median'] = sum(numbers[h]) / len(numbers[h])

    for num in numbers:
        result['arithmetic'] += num
        if no_zero_flag:
            result['geometric'] *= num
            result['harmonic'] += 1 / num
    result['arithmetic'] /= n

    if no_zero_flag:
        result['geometric'] **= 1 / n
        result['harmonic'] = n / result['harmonic']

    return result


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}

# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

