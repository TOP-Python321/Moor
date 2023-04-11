user_num = int(input("Введите трехзначное число: "))

# КОММЕНТАРИЙ: цифра — digit, число — number, num
num = user_num // 10
first_num = num // 10
second_num = num % 10
third_num = user_num % 10

sum_num = first_num + second_num + third_num
# КОММЕНТАРИЙ: произведение — product, multiply — умножить, умножать
multiply_num = first_num * second_num * third_num

print(f"Сумма цифр = {sum_num} \n"
      f"Произведение цифр = {multiply_num}")

# Сумма цифр = 16
# Произведение цифр = 140


# ИТОГ: отлично — 4/4
