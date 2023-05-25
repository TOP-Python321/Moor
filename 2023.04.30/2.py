# КОММЕНТАРИЙ: оригинальный метод защиты кода ))
fruits = "".split()

while True:
    fruit = input("Введите название фрукта: ")
    if len(fruit) > 0:
        fruits.append(fruit)
    else:
        break

if len(fruits) >= 2:
    # УДАЛИТЬ: добавлять новые элементы — плохая идея; согласитесь, что 'и' на фрукт не тянет
    fruits.insert(-1, "и")
    for elem in range(0, len(fruits) - 3):
        # УДАЛИТЬ: менять значения элементов — плохая идея; задача стояла в, дословно: "генерировании форматированной строки"
        # КОММЕНТАРИЙ: к тому же эта часть вашего кода превратится в тыкву, стоит заменить входной список на кортеж — на перспективу об этом тоже неплохо бы думать
        fruits[elem] = fruits[elem] + ","

# КОММЕНТАРИЙ-подсказка: решение второй части задачи укладывается в одну строчку кода, немного похожую на эту
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


# ИТОГ: нужно лучше, доработать — 1/3
