first_cell = input("Укажите первую клетку: ")
second_cell = input("Укажите вторую клетку: ")

first_difference = ord(first_cell[0]) - ord(second_cell[0])
second_difference = int(first_cell[1]) - int(second_cell[1])

# КОММЕНТАРИЙ: скобки не влияют на порядок выполнения операций и могут быть опущены
if (-1 <= first_difference <= 1) and (-1 <= second_difference <= 1):
    print("Да")
else:
    print("Нет")


# Укажите первую клетку: d3
# Укажите вторую клетку: e4
# Да

# Укажите первую клетку: d2
# Укажите вторую клетку: f3
# Нет

# ИТОГ: отлично — 4/4
