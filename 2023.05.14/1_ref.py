def strong_password(password: str) -> bool:
    markers = {
        'length': -7,
        'low_case': 0,
        'up_case': 0,
        'digits': -1,
        'other': 0,
    }
    for char in password:
        markers['length'] += 1
        if char.islower():
            markers['low_case'] += 1
        elif char.isupper():
            markers['up_case'] += 1
        elif char.isdigit():
            markers['digits'] += 1
        else:
            markers['other'] += 1

    for marker in markers.values():
        if marker <= 0:
            return False
    else:
        return True


# >>> strong_password('aaaaBBBB12!')
# True
# >>> strong_password('aaBB12!')
# False
# >>> strong_password('aaaaBBBB1!')
# False
# >>> strong_password('aaaaBBBB12')
# False
# >>> strong_password('AAAABBBB12')
# False
# >>> strong_password('aaaabbbb12')
# False
# >>> strong_password('жжжжЩЩЩЩ45?')
# True

