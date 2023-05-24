
number = int(input("Введите целое число: "))

divider = 1
sum_of_dividers = 0

# КОММЕНТАРИЙ: вот это хорошо оптимизированный алгоритм, молодец!
while divider ** 2 <= number:
    if number % divider == 0:
        # ИСПРАВИТЬ: только вот в ситуации, когда квадрат делителя равен исходному числу, вы добавляете этот делитель дважды (см. пример ниже)
        sum_of_dividers += divider
        if divider ** 2 != number:
            sum_of_dividers += number // divider
    divider += 1

print(sum_of_dividers)


# Введите целое число: 50
# 93

# Введите целое число: 80
# 186

# Введите целое число: 49
# 57
# КОММЕНТАРИЙ: а должно быть 57 (легко проверить вручную)


# ИТОГ: хорошо, но нужно доработать — 4/6
