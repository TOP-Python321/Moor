digit1 = int(input("Первое число: "))
digit2 = int(input("Второе число: "))

if digit1 % digit2 == 0:
    print(f"{digit1} делится на {digit2} нацело \n"
          f"частное: {digit1 // digit2}")
else:
    print(f"{digit1} не делится на {digit2} нацело \n"
          f"неполное частное: {digit1 // digit2} \n"
          f"остаток: {digit1 % digit2}")
    
# 20 делится на 5 нацело
# частное: 4

# 17 не делится на 3 нацело
# неполное частное: 5
# остаток: 2