# Exercice 1

def a_doublon(tab):
    """
    :param tab: tableau d'entiers
    :return: True si le tableau contient un doublon, False sinon
    """
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i != j and tab[i] == tab[j]:
                return True
    return False


assert a_doublon([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert a_doublon([]) == False
assert a_doublon([1]) == False
assert a_doublon([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == True
assert a_doublon([1, 2, 4, 6, 6]) == True


# Exercice 2

def voisinage(n, ligne, colonne):
    """
    Retourne la liste des voisins de la case (ligne, colonne) dans une grille de taille n
    :param n:
    :param ligne:
    :param colonne:
    :return:
    """
    voisins = []
    for l in range(max(0, ligne - 1), min(n, ligne + 2)):
        for c in range(max(0, colonne - 1), min(n, colonne + 2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l, c))
    return voisins


def incremente_voisins(grille, ligne, colonne):
    """
    Incrémente les voisins de la case (ligne, colonne) de la grille
    :param grille:
    :param ligne:
    :param colonne:
    :return:
    """
    voisins = voisinage(len(grille), ligne, colonne)

    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1


def genere_grille(bombes):
    """
    :param bombes: Liste de tuples (x, y) représentant les coordonnées de bombes
    :return: grille de jeu
    """
    n = len(bombes)
    grille = [[0 for _ in range(n)] for _ in range(n)]

    for l, c in bombes:
        grille[l][c] = -1
        incremente_voisins(grille, l, c)

    return grille


assert genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) == [[1, 1, 1, 0, 0],
                                           [1, -1, 1, 1, 1],
                                           [2, 2, 3, 2, -1],
                                           [1, -1, 2, -1, 3],
                                           [1, 1, 2, 2, -1]]
