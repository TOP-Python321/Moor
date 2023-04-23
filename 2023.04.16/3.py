year = int(input("Укажите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Да")
else:
    print("Нет")


# Да


# ИТОГ: отлично — 3/3
