base = 80
meter_tariff = 6 / 150
wait_tariff = 3


def taxi_cost(distance: int, wait_time: int = 0) -> int | None:
    if distance < 0 or wait_time < 0:
        return None
    return round(
        base
        + base * (not bool(distance))
        + distance * meter_tariff
        + wait_time * wait_tariff
    )


# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None
