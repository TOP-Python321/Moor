from collections.abc import Iterable


def tree_leaves(data: Iterable) -> int:
    """
    Функция считает количество элементов не являющимися объектом типа List.
    
    :param data: Итерируемый объект.
    
    :return: Целое число. Количество элементов.
    """
    count = 0
    
    for elem in data:
        if isinstance(elem, list):
            count += tree_leaves(elem)
        else:
            count += 1
            
    return count
    
    
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 42
# >>>
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 46