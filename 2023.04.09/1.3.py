minutes_input = int(input("Укажите количество минут: "))

hour = minutes_input // 60
minute = minutes_input % 60

print(f"{minutes_input} мин - это {hour} час {minute} мин")