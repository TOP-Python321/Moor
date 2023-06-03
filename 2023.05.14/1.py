def strong_password(password: str) -> bool:
    """
    Returns True if the string meets all conditions. 
    Otherwise return False
    """    
    upper_letter = False
    lower_letter = False
    # Правильно или нет, ограничился только этим набором символов
    # ИСПРАВИТЬ: корректнее было бы сделать множества символов букв и цифр — всё, что в них не входит, это доп.символы
    symbols = [chr(sym) for sym in range(33, 48)]
    special = False
    digit = False
    count = 0

    # ПЕРЕИМЕНОВАТЬ: имена i, j, k — только для индексов!
    for i in password:
        # УДАЛИТЬ: думается мне, что первые две проверки избыточны на каждом символе
        if i.islower():
            lower_letter = True
        elif i.isupper():
            upper_letter = True
        # ИСПОЛЬЗОВАТЬ: мы ожидаем, что в special будет объект bool, верно? тогда ничего не мешает сразу результат вычисления логического выражения присвоить в эту переменную, без лишних проверок
        # special = i in symbols
        elif i in symbols:
            special = True
        elif i.isdigit():
            digit = True
            count += 1

    # ИСПОЛЬЗОВАТЬ: я бы регистры проверял так:
    lower_letter = password != password.upper()
    upper_letter = password != password.lower()
    # КОММЕНТАРИЙ: надо бы, конечно, фактическую скорость выполнения замерить для обоих вариантов — впрочем, на коротких строках разница во времени скорее всего будет минимальна

    # ИСПРАВИТЬ: тоже if...else избыточен — сразу возвращайте вычисленный объект bool
    if (
            len(password) >= 8
        and upper_letter 
        and lower_letter 
        and special 
        and digit 
        and count > 1
    ):
        return True
    else:
        return False


# >>> strong_password("Qwer*ty12")
# True

# >>> strong_password("Pass9&word")
# False


# ИТОГ: хорошо, немного доработать — 3/4
