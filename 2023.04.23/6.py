ticket = input("Укажите номер билета: ")
number = [int(num) for num in ticket]

if sum(number[:3]) == sum(number[3:]):
    print("Да")
else: 
    print("Нет")
    

# Укажите номер билета: 585585
# Да

# Укажите номер билета: 256365
# Нет