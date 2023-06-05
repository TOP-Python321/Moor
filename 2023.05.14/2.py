def taxi_cost(distance: int, waiting_time: int = 0) -> int | None:
    # ИСПОЛЬЗОВАТЬ везде: никаких символов конца строк посередине предложений в документации и комментариях, и между предложениями об одном и том же тоже не нужны — только для подразделов длинной документации! все используют перенос строк и прекрасно читают длинные строки
    """
    Returns the cost of the trip and the waiting time (if any) if the distance is > 0. If the distance == 0, returns the fine, the start and the waiting time (if any). Otherwise returns None
    """
    start = 80
    fine = 80
    price_per_distance = distance * 6 // 150
    price_per_waiting = waiting_time * 3

    total = start + price_per_distance + price_per_waiting

    # ИСПРАВИТЬ: а нужна ли эта проверка? всегда думал, что ноль при умножении и делении на любые другие числа даёт ноль
    if distance == 0:
        total = start + fine + price_per_waiting
    # ИСПРАВИТЬ: почему только расстояние? (см. пример ниже)
    # ИСПРАВИТЬ: ещё такой момент: если вам были переданы отрицательные числа, то надо ли проводить вычисления выше? такого рода проверки должны быть в самом начале тела функции: чуть что — return None
    elif distance < 0:
        total = None
    
    return total 


# print(taxi_cost(0, 12))
# 196

# print(taxi_cost(-90, 21))
# None

# print(taxi_cost(2160, 8))
# 188

# taxi_cost(1000)
# 120
# КОММЕНТАРИЙ: тоже так хочу: таксист ждал меня минус десять минут, а я заплатил меньше
# taxi_cost(1000, -10)
# 90


# ИТОГ: можно лучше, доработать — 2/4
