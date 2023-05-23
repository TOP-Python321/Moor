digit1 = int(input("Первое число: "))
digit2 = int(input("Второе число: "))

# КОММЕНТАРИЙ: остаток (матем.) — remainder, rem; частное (матем.) — quotient
result = digit1 % digit2
total = digit1 // digit2

# КОММЕНТАРИЙ: вот! то, что надо — молодцом =)
insert1, insert2, insert3 = '', '', ''
if result:
    insert1 = 'не '
    insert2 = 'неполное '
    insert3 = f'\nостаток: {result}'

answer = (f"{digit1} {insert1}делится на {digit2} нацело\n"
          f"{insert2}частное: {total}"
          f"{insert3}")
print(answer)


# 20 делится на 5 нацело
# частное: 4

# 17 не делится на 3 нацело
# неполное частное: 5
# остаток: 2


# ИТОГ: отлично — 3/3
