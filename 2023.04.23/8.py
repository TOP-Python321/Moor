count = int(input("Укажите количество чисел последовательности: "))

fibonacci = []
num = next_num = 1

while count > 0:
    fibonacci.append(num)
    num, next_num = next_num, num + next_num
    count -= 1
    
print(*fibonacci)


# Укажите количество чисел последовательности: 20
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


# ИТОГ: отлично — 4/4
