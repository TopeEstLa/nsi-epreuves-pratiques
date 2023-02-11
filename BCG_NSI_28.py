# Exercice 1

def moyenne(tab):
    """
    Calcule la moyenne des éléments d'un tableau.
    :param tab:
    :return:
    """
    somme = 0
    for element in tab:
        somme += element
    return somme / len(tab)


assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5


# Exercice 2


def dichotomie(tab, x):
    """
    Recherche dichotomique
    :param tab:
    :param x:
    :return:
    """
    if len(tab) == 0:
        return False, 1

    if x < tab[0] or x > tab[-1]:
        return False, 2

    start = 0
    end = len(tab) - 1

    while start <= end:
        mid = (start + end) // 2
        if tab[mid] == x:
            return True
        elif x > tab[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False, 3


assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == (False, 2)
assert dichotomie([], 28) == (False, 1)