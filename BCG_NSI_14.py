# Exercice 1

def recherche(value, tab):
    """
    i renvoie l’indice de la première occurrence de value dans tab, ou -1 si value n’est pas dans tab.
    :param value:
    :param tab:
    :return i: l'indice de la première occurrence de value dans tab, ou -1 si value n’est pas dans tab.
    """
    i = 0
    for elt in tab:
        if elt == value:
            return i
        i += 1
    return -1


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3
assert recherche(50, []) == -1
assert recherche(4, [2, 4, 4, 3, 4]) == 1


# Exercice 2

def insere(a, tab):
    """
    insere a dans tab en conservant l’ordre croissant
    :param a:
    :param tab:
    :return: nouvelle liste avec a inséré
    """
    l = list(tab)
    l.append(a)
    i = len(l) - 1
    while i > 0 and l[i - 1] > l[i]:
        l[i - 1], l[i] = l[i], l[i - 1]
        i -= 1
    return l


assert insere(3, [1, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert insere(30, [1, 2, 7, 12, 14, 25]) == [1, 2, 7, 12, 14, 25, 30]
assert insere(1, [2, 3, 4]) == [1, 2, 3, 4]
assert insere(1, []) == [1]
