def numbers_strip(
        numbers: list[float],
        n: int = 1,
        *,
        copy: bool = False
) -> list[float]:
    if copy:
        numbers = numbers.copy()

    # предпочтительный способ при n < 3
    # for _ in range(n):
    #     numbers.remove(min(numbers))
    #     numbers.remove(max(numbers))

    # предпочтительный способ при n > 3
    to_remove = sorted(numbers)
    to_remove = to_remove[:n] + to_remove[-n:]
    for num in to_remove:
        numbers.remove(num)

    return numbers


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True

# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False

