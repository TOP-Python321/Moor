bin_num = input("Введите двоичное число: ")

if set(bin_num) <= {"1", "0", "b"}:
    # КОММЕНТАРИЙ: ох, накрутили проверок... есть такой эмпирический способ оптимизации кода: каждый раз когда у вас возникает третий подряд уровень вложенности условий (and — это те же вложенные условия), задавайте себе вопрос: "точно-точно-точно нельзя проще?" — в 95–97% случаев окажется, что можно =)
    if bin_num == "0b" or bin_num == "b":
        print("Нет")
    elif set(bin_num[2:]) <= {"1", "0"} and \
       {bin_num[:2]} != {"1b"} and \
       {bin_num[:2]} != {"bb"}:
        print("Да")    
    else:
        print("Нет")        
else:
    print("Нет")

# ИСПОЛЬЗОВАТЬ: пожалуй, я просто оставлю здесь более короткий вариант, а вы его сами осмыслите и прокомментируете во время работы над ошибками:
answer = 'нет'
if set(bin_num[2:]) <= {'0', '1'}:
    if bin_num[:2] in {'01', '10', 'b1', 'b0', '0b'}:
        answer = 'да'
print(answer)


# Введите двоичное число: 1b010110
# Нет

# Введите двоичное число: 0b101100
# Да

# Введите двоичное число: 010b1010
# Нет


# ИТОГ: хорошо, но можно лучше — 2/3
