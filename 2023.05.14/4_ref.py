def countable_nouns(number: int, words: tuple[str, str, str]) -> str:
    last_digit = number % 10
    if number % 100 // 10 != 1:
        if last_digit == 1:
            return words[0]
        elif last_digit in (2, 3, 4):
            return words[1]
    return words[2]


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'

