num = int(input("Введите целое число: "))

# КОММЕНТАРИЙ: с учётом дальнейшего использования f-строк и простоты операции объявление данных переменных избыточно
prev_num = num - 1
next_num = num + 1

# ИСПОЛЬЗОВАТЬ: перенос строковых литералов внутри скобок
print(f"Следующее за числом {num} число: {next_num} \n"
      f"Для числа {num} предыдущее число: {prev_num}")

# Следующее за числом 48 число: 49
# Для числа 48 предыдущее число: 47


# ИТОГ: отлично — 3/3
