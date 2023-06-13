def countable_nouns(number: int, words: tuple[str, str, str]) -> str:
    """
    Returns one word out of three passed as the second argument 'words'
    that matches the number passed as the first argument.
    """
    last_digit = number % 10
    
    if last_digit == 1 and number % 100 not in [11, 12, 13, 14]:
        return words[0]
    elif last_digit in [2, 3, 4] and number % 100 not in [11, 12, 13, 14]:
        return words[1]
    # ИСПРАВИТЬ: как бы вот этот блок else логически объединить с самым первым блоком if, в котором возвращается такое же значение? может и проверок получится поменьше
    else:
        return words[2]


# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(331, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(126, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(874, ("год", "года", "лет"))
# 'года'


# ИТОГ: хорошо, немного доработать — 3/4
