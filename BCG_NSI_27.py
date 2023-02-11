# Exercice 1

def recherche_min(tab):
    """
    Recherche l'indice du minimum dans un tableau.
    :param tab:
    :return:
    """
    last_min = 0
    for i in range(len(tab)):
        if tab[i] < tab[last_min]:
            last_min = i
    return last_min


assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2


# Exercice 2

def separe(tab):
    """
    Sépare les 0 et les 1 dans un tableau et replace les 0 à gauche et les 1 à droite.
    :param tab:
    :return:
    """
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche += 1
        else:
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite -= 1
    return tab


assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
