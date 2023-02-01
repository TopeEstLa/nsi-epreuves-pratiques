# Exercice 1

def moyenne(tab):
    """
    Retourne la moyenne des éléments du tableau.
    :param tab: tableau d'entiers
    :return: moyenne des éléments du tableau
    """
    somme = 0
    somme_poids = 0
    for element in tab:
        somme += element[0] * element[1]
        somme_poids += element[1]

    if (somme_poids == 0):
        return None

    return somme / somme_poids


assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5


# Exercice 2

def pascal(n):
    """
    Retourne le triangle de Pascal jusqu'à la ligne n.
    :param n:
    :return:
    """
    triangle = [[1]]
    for k in range(1, n+1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k - 1][i - 1] + triangle[k - 1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle


assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
