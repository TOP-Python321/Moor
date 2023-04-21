digit1 = input("Первое число: ")
digit2 = input("Второе число: ")
digit3 = input("Третье число: ")

sum_of_positive = 0
    
if digit1.isdecimal():
    sum_of_positive += int(digit1)
elif float(digit1) > 0:
    sum_of_positive += float(digit1)
    
if digit2.isdecimal():
    sum_of_positive += int(digit2)
elif float(digit2) > 0:
    sum_of_positive += float(digit2)
    
if digit3.isdecimal():
    sum_of_positive += int(digit3)
elif float(digit3) > 0:
    sum_of_positive += float(digit3)

print(sum_of_positive) 

# Первое число: 5
# Второе число: 63
# Третье число: 2.9
# 70.9

# Первое число: 5
# Второе число: -9
# Третье число: 6
# 11