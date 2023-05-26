server_errors = {}

while True:
    user_input = input("Введите код ошибки и значение: ").split()

    if len(user_input) > 1:
        # УДАЛИТЬ: переменная input_errors избыточна
        server_errors[user_input[0]] = user_input[1]
    elif len(user_input) == 0:
        break
    else:
        user_input = user_input[0]
        found = False
        for key, value in server_errors.items():
            if value == user_input:
                found = True
                print(key)
                break
        if not found:
            print("! value error !")
            break

    # ИСПРАВИТЬ: не так: сначала отрабатывает цикл пополнения словаря (до ввода пустой строки)
            # ДОБАВИТЬ: вывод "! value error !" должен быть здесь, на случай, если ключ не найден
        
        # УДАЛИТЬ: а этот блок может обработать ошибку ввода (которой в этой задаче можно пренебречь) — но не ошибку поиска ключа по значению
        
    
    
# Введите код ошибки и значение: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите код ошибки и значение: 4108 ER_GIPK_COLUMN_EXISTS
# Введите код ошибки и значение: 1004 ER_CANT_CREATE_FILE
# Введите код ошибки и значение: ER_GIPK_COLUMN_EXISTS
# 4108
# УДАЛИТЬ: у вас нет этого вывода при вводе выше — не ленитесь проверять


# Введите код ошибки и значение: 4108 ER_GIPK_COLUMN_EXISTS
# Введите код ошибки и значение: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите код ошибки и значение: 1004 ER_CANT_CREATE_FILE
# Введите код ошибки и значение: ER_CANT_CREATE_DB
# ! value error !


# ИТОГ: доработать — 1/3
