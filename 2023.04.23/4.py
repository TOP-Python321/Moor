# Оптимизировал скорость выполнения программы, так как в первом варианте очень долго считались числа, если разрядность была больше 3
# через time посчитал, что скорость подсчета 5 разряда была 91 секунда, теперь - 0.021 секунды
# использовал решето Эратосфена. Знаю, что не проходили это, просто решил попробовать этот метод.
# ниже есть первый вариант.

rank = int(input("Укажите разряд: "))

max_number = int("9" * rank)
min_number = (max_number + 1) // 10
count = 0

# ОТВЕТИТЬ: это-то, конечно, лучший алгоритм — а вы поняли, как и почему он работает?

prime = [True] * (max_number + 1) # Создаем список, в котором каждый элемент True
prime[0] = prime[1] = False # Первый и второй элемент устанавливаем в False, так как они не простые числа. При разрядности равной 3, это будут числа 999 и 1000
for i in range(2, max_number + 1): 
    if not prime[i]: # Если элемент списка имеет значение False, то итерация продолжается. Иначе выполнится цикл for
        continue
    for j in range(i*i, max_number+1, i): # Проходим циклом по всем элементам списка кратным prime[i]
        prime[j] = False # и устанавливаем их значение в False

# ИСПОЛЬЗОВАТЬ: если нужно только количество вычислить, а сами числа не нужны, то лучше так сделать:
primes = sum(prime[i] for i in range(min_number, max_number+1)) # Тут я затупил и нужно было посчитать длину списка.
# primes = len([i for i in range(min_number, max_number+1) if prime[i]])

print(primes)


# Укажите разряд: 4
# 1061


# Изначальный вариант
# rank = int(input("Укажите разряд: "))
# max_number = int("9" * rank)
# min_number = (max_number + 1) // 10
# count = 0
# for num in range(min_number, max_number + 1):
    # КОММЕНТАРИЙ: вот здесь нужно было использовать алгоритм нахождения делителей из прошлой задачи: такой производительности как в решете Эратосфена не получили бы, но в 4–5 раз тоже неплохо, 6 разрядов за 10–15 с обсчитывает — а здесь у вас куча итераций лишних с проверками на каждой: ясно дело, тормозит
    # for i in range(2, num): 
        # if(num % i) == 0: 
            # break 
    # else: 
        # count += 1
# print(count)        


# Укажите разряд: 4
# 1061


# ИТОГ: отлично — 6/6
