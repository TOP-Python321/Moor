from random import randrange


def tree_generator() -> list:
    """
    Функция генерирует дерево с произвольным количеством веток и листьев.
    
    :return: Список. Сгенерированное дерево.
    """
    tree = []
    elems = [[], 'leaf', 'leaf']

    if randrange(2):
        tree += [elems[randrange(3)]] * randrange(1, 5) 
    else:
        loop = randrange(3) + 1
        for i in range(loop):
            branch = tree_generator()
            tree.append(branch)
    
    return tree
    
    
# >>> tree_generator()
# [['leaf', 'leaf', 'leaf'], [[[[['leaf', 'leaf', 'leaf', 'leaf'], [[[], [], []]]]], ['leaf']], [['leaf', 'leaf', 'leaf'], [['leaf', 'leaf', 'leaf'], [[]], [[[], [], []], [['leaf', 'leaf', 'leaf']], [['leaf', 'leaf', 'leaf', 'leaf']]]]]], ['leaf']]

# >>> tree_generator()
# [['leaf', 'leaf', 'leaf'], [[], []]]

# >>> tree_generator()
# [[]]