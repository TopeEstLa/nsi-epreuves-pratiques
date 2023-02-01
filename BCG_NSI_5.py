# Exercice 1

def lancer(n):
    """
    Retourne la liste des résultats de n nombre aléatoire entre 1 et 6.
    :param n:
    :return:
    """
    import random
    return [random.randint(1, 6) for _ in range(n)]


assert lancer(0) == []
assert len(lancer(1)) == 1


def paire_6(tab):
    """
    Retourne True si le tableau contient deux 6.
    :param tab:
    :return:
    """
    count = 0
    for i in range(len(tab)):
        if tab[i] == 6:
            count += 1

            if count >= 2:
                return True

    return False


assert paire_6([5, 6, 6, 2, 2]) == True
assert paire_6([6, 5, 1, 6, 6]) == True
assert paire_6([5, 6, 6, 6, 2, 2]) == True
assert paire_6([5, 6, 2, 2]) == False
assert paire_6([2, 2, 6]) == False
assert paire_6([5, 6, 3, 2, 6]) == True

# Exercice 2
img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],
       [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]


def nbLig(image):
    """
    Retourne le nombre de ligne de l'image.
    :param image:
    :return:
    """
    return len(image)


assert nbLig(img) == 4


def nbCol(image):
    """
    Retourne le nombre de colonne de l'image.
    :param image:
    :return:
    """
    return len(image[0])


assert nbCol(img) == 5


def negatif(image):
    """
    Retourne une image négatif de l'image.
    :param image:
    :return:
    """
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]

    return L


def negatif_v2(image):
    """
    Retourne une image négatif de l'image, mais en une ligne.
    :param image:
    :return:
    """
    return [[255 - image[i][j] for j in range(nbCol(image))] for i in range(nbLig(image))]


assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert negatif_v2(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168],
                           [0, 255, 231, 58, 66]]


def binaire(image, seuil):
    """
    Retourne une image binaire de l'image.
    :param image:
    :return:
    """
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] > seuil:
                L[i][j] = 1
            else:
                L[i][j] = 0

    return L


assert binaire(img, 120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]
