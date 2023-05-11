server_errors = {}

while True:
    user_input = input("Введите код ошибки и значение: ").split()

    if len(user_input) > 1:
        input_errors = {user_input[0]: user_input[1]}
        server_errors |= input_errors
    elif len(user_input) == 1:
        user_input = " ".join(user_input)
        for key, value in server_errors.items():
            if value == user_input:
                print(key)
        break
    else:
        print("! value error !")
        break
    
    
# Введите код ошибки и значение: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите код ошибки и значение: 4108 ER_GIPK_COLUMN_EXISTS
# Введите код ошибки и значение: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# Введите код ошибки и значение: ER_CANT_OPEN_FILE
# ! value error !

# Введите код ошибки и значение: 1004 ER_CANT_CREATE_FILE
# Введите код ошибки и значение: 1006 ER_CANT_CREATE_DB
# Введите код ошибки и значение: 1007 ER_DB_CREATE_EXISTS
# Введите код ошибки и значение: 1010 ER_DB_DROP_RMDIR
# Введите код ошибки и значение: ER_CANT_CREATE_FILE
# 1004