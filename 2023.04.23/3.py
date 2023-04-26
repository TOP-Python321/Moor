digit = int(input("Введите целое число: "))

devider = 1
sum_of_deviders = 0

while devider ** 2 <= digit:
    if digit % devider == 0:
        sum_of_deviders += devider + digit // devider
    devider += 1
            
print(sum_of_deviders)


# Введите целое число: 50
# 93

# Введите целое число: 80
# 186