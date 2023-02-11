# Exercice 1

def moyenne(tab):
    """
    Calcule la moyenne des éléments d'un tableau.
    :param tab:
    :return:
    """
    if len(tab) == 0:
        return 0

    somme = 0
    for element in tab:
        somme += element
    return somme / len(tab)


assert moyenne([5, 3, 8]) == 5.333333333333333
assert moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
assert moyenne([]) == 0


# Exercice 2

def tri(tab):
    """
    i est le premier indice de la zone non triée,
    j est le dernier indice de cette zone non triée.
    Au début, la zone non triée est le tableau complet.

    :param tab:
    :return:
    """
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab


assert tri([0, 1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]
