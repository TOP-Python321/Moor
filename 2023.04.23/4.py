rank = int(input("Укажите разряд: "))

max_number = int("9" * rank)
min_number = (max_number + 1) // 10
count = 0

for num in range(min_number, max_number + 1): 
    for i in range(2, num): 
        if(num % i) == 0: 
            break 
    else: 
        count += 1

print(count)        

# Укажите разряд: 4
# 1061