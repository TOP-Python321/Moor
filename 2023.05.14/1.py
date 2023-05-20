def strong_password(password: str) -> bool:
    """
    Returns True if the string meets all conditions. 
    Otherwise return False
    """    
    upper_letter = False
    lower_letter = False
    symbols = "@#$%^&*+="
    special = False
    digit = False
    count = 0
    
    for i in password:
        if i.islower():
            lower_letter = True
        elif i.isupper():
            upper_letter = True
        elif i in symbols:
            special = True
        elif i.isdigit():
            digit = True
            count += 1
    
    if (len(password) >= 8 
        and upper_letter 
        and lower_letter 
        and special 
        and digit 
        and count > 1):
        return True
    else:
        return False


# >>> strong_password("Qwer*ty12")
# True

# >>> strong_password("Pass9&word")
# False