# Exercice 2

def indices_maxi(tab):
    """
    Retourne les indices du maximum du tableau.
    :param tab: tableau d'entiers
    :return: liste des indices du maximum
    """
    maxi = tab[0]
    indices = [0]

    for i in range(1, len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indices = [i]
        elif tab[i] == maxi:
            indices.append(i)

    return (maxi, indices)


assert indices_maxi([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (10, [9])
assert indices_maxi([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == (10, [9, 10])
assert indices_maxi([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == (10, [9])
assert indices_maxi([10, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (10, [0, 9])


# Exercice 2

def positif(pile):
    """
    Retourne une pile contenant uniquement les éléments positifs.
    :param pile:
    :return: pile contenant uniquement les éléments positifs
    """
    pile_1 = list(pile)
    pile_2 = []

    while len(pile_1) > 0:
        element = pile_1.pop()
        if element >= 0:
            pile_2.append(element)

    while len(pile_2) > 0:
        pile_1.append(pile_2.pop())

    return pile_1


assert positif([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positif([-1, 2, 3, 4, -5, 6, 7, 8, -9, -10, 10]) == [2, 3, 4, 6, 7, 8, 10]
assert positif([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == []
