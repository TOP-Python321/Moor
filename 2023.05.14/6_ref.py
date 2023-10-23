def orth_triangle(
        *,
        cath1: float = 0,
        cath2: float = 0,
        hypo: float = 0
) -> float | None:
    if 0 < cath1 and 0 < cath2 and hypo == 0:
        return (cath1**2 + cath2**2)**0.5
    elif 0 < cath1 < hypo and cath2 == 0:
        return (hypo**2 - cath1**2)**0.5
    elif 0 < cath2 < hypo and cath1 == 0:
        return (hypo**2 - cath2**2)**0.5
    else:
        return None


# >>> orth_triangle(cath1=3, cath2=4)
# 5.0
# >>> orth_triangle(cath1=3, hypo=5)
# 4.0
# >>> orth_triangle(cath2=4, hypo=5)
# 3.0

# >>> print(orth_triangle(cath1=3, cath2=4, hypo=5))
# None
# >>> print(orth_triangle(cath1=3, cath2=-4))
# None

