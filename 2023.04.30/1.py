email = input("Введите адрес электронной почты: ")

# так же добавил проверку, что первый символ не должен быть @
if email.count("@") == 1 \
    and email[0] != "@" \
    and email.count(".") > 0 \
    and email.rfind(".") > email.find("@") + 1:
    print("да")
else:
    print("нет")
    
# Введите адрес электронной почты: exam@mail.ru
# да

# Введите адрес электронной почты: exam.exam@mail
# нет