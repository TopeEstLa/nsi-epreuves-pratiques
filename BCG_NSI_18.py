# Exercice 1

def max_et_indice(tab):
    """
    Retourne le maximum et l'indice correspondant.
    :param tab:
    :return: couple (maximum, indice)
    """
    max_index = 0
    for i in range(1, len(tab)):
        if tab[i] > tab[max_index]:
            max_index = i
    return tab[max_index], max_index


assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)

# Exercice 2


