# Exerice 1

def multiplication(n1, n2):
    """
    Retourne le produit de n1 et n2 avec seulement des additions et des soustractions.
    :param n1:
    :param n2:
    :return:
    """
    if n1 == 0 or n2 == 0:
        return 0

    if n1 < 0:
        return -multiplication(-n1, n2)

    if n2 < 0:
        return -multiplication(n1, -n2)

    return n1 + multiplication(n1, n2 - 1)


assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0


# Exercice 2

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None

    m = (i + j) // 2

    if tab[m] < n:
        return chercher(tab, n, m + 1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m - 1)
    else:
        return m


assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) is None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) is None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
