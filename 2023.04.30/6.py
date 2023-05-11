bin_num = input("Введите двоичное число: ")

if set(bin_num) <= {"1", "0", "b"}:
    if bin_num == "0b" or bin_num == "b":
        print("Нет")
    elif set(bin_num[2:]) <= {"1", "0"} and \
       {bin_num[:2]} != {"1b"} and \
       {bin_num[:2]} != {"bb"}:
        print("Да")    
    else:
        print("Нет")        
else:
    print("Нет")
    
# Введите двоичное число: 1b010110
# Нет

# Введите двоичное число: 0b101100
# Да

# Введите двоичное число: 010b1010
# Нет