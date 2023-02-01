# Exercice 1

def recherche(tab, x):
    """
    Retourne l'indice de la dernière occurrence de x dans tab.
    :param tab:
    :param x:
    :return:
    """
    lastOccurrence = -1

    for i in range(len(tab)):
        if tab[i] == x:
            lastOccurrence = i

    return lastOccurrence if lastOccurrence != -1 else len(tab)


assert recherche([5, 3], 1) == 2
assert recherche([5, 3], 5) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3

# Exercice 2

from math import sqrt


def distance(point1, point2):
    """
    Retourne la distance entre les deux points.
    :param point1:
    :param point2:
    :return: distance entre les deux points
    """
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


assert distance((1, 0), (5, 3)) == 5.0
assert distance((1, 0), (0, 1)) == 1.4142135623730951


def plus_courte_distance(tab, depart):
    """
    Retourne la distance entre le point et le point le plus proche de lui dans le tableau.
    :param tab:
    :param depart:
    :return:
    """
    point = tab[0]
    min_distance = distance(tab[0], depart)

    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_distance:
            point = tab[i]
            min_distance = distance(tab[i], depart)

    return point


assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5)
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)) == (5, 2)
