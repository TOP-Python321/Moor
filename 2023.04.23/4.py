# Оптимизировал скорость выполнения программы, так как в первом варианте очень долго считались числа, если разрядность была больше 3
# через time посчитал, что скорость подсчета 5 разряда была 91 секунда, теперь - 0.021 секунды
# использовал решето Эратосфена. Знаю, что не проходили это, просто решил попробовать этот метод.
# ниже есть первый вариант.

rank = int(input("Укажите разряд: "))

max_number = int("9" * rank)
min_number = (max_number + 1) // 10
count = 0

prime = [True] * (max_number + 1)
prime[0] = prime[1] = False
for i in range(2, max_number + 1):
    if not prime[i]:
        continue
    for j in range(i * i, max_number + 1, i):
        prime[j] = False
primes = len([i for i in range(min_number, max_number + 1) if prime[i]])
print(primes)

# Укажите разряд: 4
# 1061


# Изначальный вариант

# rank = int(input("Укажите разряд: "))

# max_number = int("9" * rank)
# min_number = (max_number + 1) // 10
# count = 0

# for num in range(min_number, max_number + 1): 
    # for i in range(2, num): 
        # if(num % i) == 0: 
            # break 
    # else: 
        # count += 1

# print(count)        

# Укажите разряд: 4
# 1061