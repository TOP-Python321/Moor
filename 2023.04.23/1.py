amount = []

while True:
    digit = int(input("Введите целое число: "))
    if digit % 7 != 0:
        print(*amount[::-1])
        break
    amount.append(digit)
    
# Введите целое число: 7
# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 23
# 21 14 7