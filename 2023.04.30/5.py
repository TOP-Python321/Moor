scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input("Введите слово: ").upper().replace("Ё", "Е")

points = 0

print(sum(points + key for letter in word for key, value in scores_letters.items() if letter in value))


# 2 вариант с циклами

# letters_count = {}
# points = 0

# for letter in list(word):
    # letters_count[letter] = letters_count.get(letter, 0) + 1
    
# for key, value in letters_count.items():
    # for score, letter in scores_letters.items():
        # if key in list(letter):
            # points += score * value
            
# print(points)

# Введите слово: неожиданность
# 20