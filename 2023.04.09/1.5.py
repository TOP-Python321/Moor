first_num = int(input("Введите целое число мили: "))
second_num = int(input("Введите дробное число мили: "))

# Решил засунуть все в переменные, чтобы функция print была более читабельна
km = 1.61
mile = float(f"{first_num}.{second_num}")
multiply = mile * km
convert = round(multiply, 1)

print(f"{mile} миль = {convert} км")

# 25.9 миль = 41.7 км