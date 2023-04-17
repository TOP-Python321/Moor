first_cell = input("Укажите первую клетку: ")
second_cell = input("Укажите вторую клетку: ")


if ord(first_cell[0]) - ord(second_cell[0]) < -1 or ord(first_cell[0]) - ord(second_cell[0]) > 1:
    print("Нет")
elif int(first_cell[1]) - int(second_cell[1]) < -1 or int(first_cell[1]) - int(second_cell[1]) > 1:
    print("Нет")
else:
    print("Да")


# Укажите первую клетку: d3
# Укажите вторую клетку: e4
# Да