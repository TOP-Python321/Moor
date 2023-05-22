def orth_triangle(cathetus1: int = 0, cathetus2: int = 0, hypotenuse: int = 0) -> float:
    """
    Return the third side of a triangle if the other two are known. 
    Return None if the calculation is not possible or if the hypotenuse 
    is greater than one of the cathetus.
    """
    if cathetus1 and cathetus2:
        hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** (1/2)
        return hypotenuse
    elif hypotenuse and cathetus1 and hypotenuse > cathetus1:
        cathetus2 = (hypotenuse ** 2 - cathetus1) ** (1/2)
        return cathetus2
    elif hypotenuse and cathetus2 and hypotenuse > cathetus2:
        cathetus1 = (hypotenuse ** 2 - cathetus2) ** (1/2)
        return cathetus1
    else:
        return None
        
        
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0

# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None

# >>> orth_triangle(cathetus1=14, cathetus2=21)
# 25.238858928247925