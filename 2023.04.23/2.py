count = int(input("Укажите количество целых чисел: "))

numbers = []
sum_of_positive = 0

while count != 0:
    digit = int(input("Введите целое число: "))
    numbers.append(digit)
    count -= 1
    
for num in numbers:
    if num >= 0:
        sum_of_positive += num
        
print(sum_of_positive)

# Укажите количество целых чисел: 6
# Введите целое число: 3
# Введите целое число: 6
# Введите целое число: -9
# Введите целое число: -9
# Введите целое число: 1
# Введите целое число: 2
# 12