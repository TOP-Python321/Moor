message = input("Введите текст сообщения: ")

symbol = 30
price = 0

for i in message.replace(" ", ""):
    price += symbol
    
print(f"{price // 100} руб. {price % 100} коп.")

# Введите текст сообщения: андрюха у нас труп возможен криминал по коням
# 11 руб. 40 коп.