fruits = "".split()

while True:
    fruit = input("Введите название фрукта: ")
    if len(fruit) > 0:
        fruits.append(fruit)
    else:
        break
        
if len(fruits) >= 2:
    fruits.insert(-1, "и")
    for elem in range(0, len(fruits) - 3):
        fruits[elem] = fruits[elem] + ","
    
print(" ".join(fruits))

# Введите название фрукта: apple
# Введите название фрукта:
# apple

# Введите название фрукта: apple
# Введите название фрукта: orange
# Введите название фрукта:
# apple и orange

# Введите название фрукта: apple
# Введите название фрукта: orange
# Введите название фрукта: cherry
# Введите название фрукта: kiwi
# Введите название фрукта:
# apple, orange, cherry и kiwi