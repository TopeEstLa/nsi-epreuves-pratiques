# Exercice 1

def couples_consecutifs(tab):
    """
    Calcule le nombre de couples consécutifs dans un tableau.
    :param tab:
    :return:
    """
    tab_term = []

    for i in range(len(tab) - 1):
        if tab[i] == tab[i + 1] - 1:
            tab_term.append((tab[i], tab[i + 1]))

    return tab_term


assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]


# Exercice 2

def propager(M, i, j, val):
    """
    Propage la valeur val dans la matrice M à partir de la case (i,j).
    :param M:
    :param i:
    :param j:
    :param val:
    :return:
    """
    if M[i][j] == 1:
        M[i][j] = val

        if i > 0:
            propager(M, i - 1, j, val)

        if j > 0:
            propager(M, i, j - 1, val)

        if i < len(M) - 1:
            propager(M, i + 1, j, val)

        if j < len(M[0]) - 1:
            propager(M, i, j + 1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
