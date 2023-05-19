def countable_nouns(number: int, words: tuple[str, str, str]) -> str:
    """
    Returns one word out of three passed as the second argument 'words'
    that matches the number passed as the first argument.
    """
    numeral = str(number)[-1]
    if int(numeral) == 1:
        return words[0]
    elif 2 <= int(numeral) <= 4:
        return words[1]
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