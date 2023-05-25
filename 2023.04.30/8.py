# ИСПРАВИТЬ: использование replace() избыточно, можно выполнять разбивку по нужной подстроке передачей аргумента в split()
files = input("Введите названия файлов через точку с запятой: ").replace("; ", " ").split()

files_list = []
files_dict = {}

for f in files:
    files_dict[f] = files_dict.get(f, 0) + 1
    # КОММЕНТАРИЙ: хорошо, что в один цикл пошли
    if files_dict[f] == 1:
        files_list.append(f)
    else:
        # ИСПРАВИТЬ: метод find() вызывается лишний раз — оптимизируйте
        files_list.append(f[:f.find(".")] + "_" + str(files_dict[f]) + f[f.find("."):])

print(*sorted(files_list), sep="\n")

# Введите названия файлов через точку с запятой: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz


# ИТОГ: хорошо, требуется немного доработать — 4/6
