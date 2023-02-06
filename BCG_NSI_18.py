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


def est_un_ordre(tab):
    """
    Détermine si un tableau est un ordre.
    :param tab:
    :return: True si le tableau est un ordre, False sinon
    """
    if tab[0] != 1 or tab[-1] != len(tab):
        return False

    for i in range(1, len(tab)):
        if tab[i] - tab[i - 1] not in [-1, 1]:
            return False
    return True


assert est_un_ordre([1, 6, 2, 8, 3, 7]) == False


# assert est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]) == True


def nombre_points_rupture(ordre):
    """
    Détermine le nombre de points de rupture d'un ordre.
    :param ordre:
    :return: nombre de points de rupture
    """
    if est_un_ordre(ordre):
        return 0

    nb_points_rupture = 0

    if ordre[0] != 1:
        nb_points_rupture += 1

    if ordre[-1] != len(ordre):
        nb_points_rupture += 1

    i = 0

    while i < len(ordre):
        if ordre[i] - ordre[i - 1] not in [-1, 1]:
            nb_points_rupture += 1
        i += 1

    return nb_points_rupture


assert nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]) == 4
assert nombre_points_rupture([1, 2, 3, 4, 5]) == 0
assert nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]) == 7
assert nombre_points_rupture([2, 1, 3, 4]) == 2