rank = int(input("Укажите разряд: "))

dozens = "0"
min_number = 1
max_number = int("9" * rank)
count = 0

if rank > 1:
    min_number = int(str(min_number) + dozens * (rank - 1))

for num in range(min_number, max_number + 1): 
    for i in range(2, num): 
        if(num % i) == 0: 
            break 
    else: 
        count += 1

print(count)        

# Укажите разряд: 4
# 1061