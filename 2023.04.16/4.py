first_cell = input("Укажите первую клетку: ")
second_cell = input("Укажите вторую клетку: ")

color1 = (ord(first_cell[0]) + int(first_cell[1])) % 2
color2 = (ord(second_cell[0]) + int(second_cell[1])) % 2

if color1 == color2:
    print("Да")
else:
    print("Нет")


# Укажите первую клетку: a3
# Укажите вторую клетку: f4
# Да


# ИТОГ: отлично — 5/5
