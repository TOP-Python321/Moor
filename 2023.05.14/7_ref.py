numbers_digits = {d: str(d) for d in range(10)} | {d: chr(d+87) for d in range(10, 36)}
digits_numbers = {v: k for k, v in numbers_digits.items()}


def int_base(number: str, from_: int, to_: int) -> str | None:
    if not 2 <= from_ <= 36 or not 2 <= to_ <= 36:
        return None
    for ch in number:
        if ch > numbers_digits[from_-1]:
            return None
    return ten_to_other(other_to_ten(number, from_), to_)
    # также можно воспользоваться встроенной функцией int()
    # return ten_to_other(int(number, from_), to_)


def other_to_ten(number: str, from_: int) -> int:
    return sum(
        digits_numbers[d] * from_**i
        for i, d in enumerate(number[::-1])
    )


def ten_to_other(number: int, to_: int) -> str:
    remainders = []
    while number:
        number, rem = divmod(number, to_)
        remainders.append(rem)
    return ''.join(numbers_digits[rem] for rem in remainders[::-1])


# >>> int_base('1101010', 2, 30)
# '3g'
# >>> int_base('1234', 5, 18)
# 'ae'
# >>> int_base('123', 4, 28)
# 'r'
# >>> int_base('111', 3, 10)
# '13'
# >>> int_base('ff00', 16, 2)
# '1111111100000000'
