# Пока не реализовал передачу вещественных чисел, постараюсь доделать
def int_base(num: str, initial: int, target: int) -> str:
    """
    Returns the string representation of the given number.
    'num' takes string notation of a number
    'initial' takes the source number system
    'target' takes the target number system
    """    
    digits ={}
    for i in range(10):
        digits[str(i)] = i 
    for i in range(65, 91):
        digits[chr(i)] = i - 55
            
    reverse_digits = {k:v for v, k in digits.items()}
            
    original_number = num.upper()
    rate = len(original_number) - 1
    decimal_digits = []
    decimal_number = 0
    target_number = ''
    
    for digit in original_number:
        decimal_digits.append(digits[digit])
    
    for i in decimal_digits:
        decimal_number += i * (initial ** rate)
        rate -= 1

    while decimal_number > 0:
        remainder_digit = decimal_number % target
        if 9 < remainder_digit < 36:
            target_number = reverse_digits[remainder_digit] + target_number
        else:
            target_number = str(remainder_digit) + target_number
        decimal_number = decimal_number // target
                
    return target_number
    
    
# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3G'
# >>> int_base('3645fe6', 16, 10)
# '56909798'