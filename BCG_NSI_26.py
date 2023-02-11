# Exercice 1

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

def dichotomie(tab, x):
    """
    Recherche dichotomique
    :param tab:
    :param x:
    :return:
    """
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
    return False


assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False
