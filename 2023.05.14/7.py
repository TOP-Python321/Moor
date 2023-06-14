# Пока не реализовал передачу вещественных чисел, постараюсь доделать
from itertools import chain
def int_base(num: str, initial: int, target: int) -> str:
    # ИСПОЛЬЗОВАТЬ: есть такой синтаксис описания параметров, называется reStructuredText, используется некоторыми IDE
    """
    Returns the string representation of the given number.

    :param num: takes string notation of a number
    :param initial: takes the source number system
    :param target: takes the target number system
    """
    digits = {}
    # ПЕРЕИМЕНОВАТЬ: имена i, j, k — только для индексов!
    for digit in range(10):
        digits[str(digit)] = digit
    for letter in range(65, 91):
        digits[chr(letter)] = letter - 55

    # ИСПОЛЬЗОВАТЬ: а ещё можно вот так:
    codes = chain(range(48, 58), range(65, 91))
    # ИСПОЛЬЗОВАТЬ: или так:
    # from itertools import chain
    # codes = chain(range(48, 58), range(65, 91))
    digits = {chr(code): i for i, code in enumerate(codes)}
    reverse_digits = {k: v for v, k in digits.items()}

    # ИСПРАВИТЬ: если переменная num в своём исходном значении больше не используется, то смело перезаписывайте её, не нужно плодить лишние сущности (переменные)
    original_number = num.upper()
    # ПЕРЕИМЕНОВАТЬ: power — частота; степень числа — power, exponent
    power = len(original_number) - 1
    decimal_digits = []
    decimal_number = 0
    target_number = ''
    
    for digit in original_number:
        decimal_digits.append(digits[digit])

    # ИСПОЛЬЗОВАТЬ: или так
    decimal_digits = [digits[ch] for ch in original_number]

    # ПЕРЕИМЕНОВАТЬ: имена i, j, k — только для индексов!
    for digit in decimal_digits:
        # ИСПОЛЬЗОВАТЬ везде: круглые скобки вокруг выражений нужны либо для многострочной записи, либо для изменения приоритетов операторов, в остальных случаях не нужны — в данном случае приоритет операторов от появления скобок не изменился
        decimal_number += digit * initial**power
        power -= 1

    # ИСПОЛЬЗОВАТЬ: или так
    decimal_number = sum(
        dig * initial**exp
        for dig, exp in zip(
            decimal_digits,
            range(len(original_number)-1, -1, -1)
        )
    )

    while decimal_number > 0:
        remainder_digit = decimal_number % target
        if 9 < remainder_digit < 36:
            target_number = reverse_digits[remainder_digit] + target_number
        else:
            target_number = str(remainder_digit) + target_number
        decimal_number = decimal_number // target

    return target_number


# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3G'
# >>> int_base('3645fe6', 16, 10)
# '56909798'


# ИТОГ: очень хорошо — 5/6
