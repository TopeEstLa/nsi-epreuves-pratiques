# Exercice 1

def renverse(mot):
    """
    Renvoie le mot renversé.
    :param mot:
    :return:
    """
    mot_renverse = ''
    for i in range(len(mot)):
        mot_renverse += mot[len(mot) - 1 - i]
    return mot_renverse


assert renverse("informatique") == "euqitamrofni"


# Exercice 2

def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits
    que n
    :param n:
    :return:
    """
    premiers = []
    tab = [True] * n
    tab[0] = False
    tab[1] = False

    for i in range(2, n):
        if tab[i]:
            premiers.append(i)
            for j in range(i * i, n, i):
                tab[j] = False
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
