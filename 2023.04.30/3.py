first_list = input("Введите список чисел: ").split()
second_list = input("Введите второй списко чисел: ").split()

for i in range(len(first_list)):
    if second_list == first_list[i:i + len(second_list)]:
        answer = "Да"
        break
    else:
        answer = "Нет"
        
print(answer)
    
# Введите список чисел: 1 2 3 5 8
# Введите второй списко чисел: 2 5
# нет

# Введите список чисел: 1 2 3 5 8
# Введите второй списко чисел: 5 8
# да

# Введите список чисел: 1 2 3 5 8
# Введите второй списко чисел:
# да