# КОММЕНТАРИЙ: оригинальный метод защиты кода ))
# это я проверял можно ли таким образом создать список и, видимо, не иправил) Придумаю оригинальнее)
fruits_list = []

while True:
    fruit = input("Введите название фрукта: ")
    
    if len(fruit) > 0:
        fruits_list.append(fruit)
    else:
        break
    

if len(fruits_list) == 1:
    # УДАЛИТЬ: добавлять новые элементы — плохая идея; согласитесь, что 'и' на фрукт не тянет
    print(fruits_list[0])
elif len(fruits_list) >= 2:
    fruits_str = ','.join(fruits_list[:-1]).replace(',',', ') + f' и {fruits_list[-1]}'
    # fruits_str += f' и {fruits_list[-1]}'
    print(fruits_str)

        # УДАЛИТЬ: менять значения элементов — плохая идея; задача стояла в, дословно: "генерировании форматированной строки"
        # КОММЕНТАРИЙ: к тому же эта часть вашего кода превратится в тыкву, стоит заменить входной список на кортеж — на перспективу об этом тоже неплохо бы думать


# КОММЕНТАРИЙ-подсказка: решение второй части задачи укладывается в одну строчку кода, немного похожую на эту



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
