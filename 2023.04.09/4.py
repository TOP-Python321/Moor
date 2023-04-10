user_num = int(input("Введите трехзначное число: "))

num = user_num // 10
first_num = num // 10
second_num = num % 10
third_num = user_num % 10

sum_num = first_num + second_num + third_num
multiply_num = first_num * second_num * third_num

print(f"Сумма цифр = {sum_num} \nПроизведение цифр = {multiply_num}")

# Сумма цифр = 16
# Произведение цифр = 140