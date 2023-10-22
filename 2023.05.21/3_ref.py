def str_round(number: float) -> str:
    return str(round(number))


def math_function_resolver(
        math_func: 'function',
        *x_values: float,
        res_to_str: bool = False
) -> list[int | str]:
    transform = str_round if res_to_str else round
    return [transform(math_func(x)) for x in x_values]


# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>>
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# >>>
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
